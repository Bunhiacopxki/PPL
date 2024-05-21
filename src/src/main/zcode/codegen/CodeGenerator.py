'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from Visitor import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from functools import reduce

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("readNumber", MType(list(), NumberType()), CName(self.libName)),
            Symbol("writeNumber", MType([NumberType()], None), CName(self.libName)),
            Symbol("readBool", MType(list(), BoolType()), CName(self.libName)),
            Symbol("writeBool", MType([BoolType()], None), CName(self.libName)),
            Symbol("readString", MType(list(), StringType()), CName(self.libName)),
            Symbol("writeString", MType([StringType()], None), CName(self.libName)),
        ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class StringType(Type):
    
    def __str__(self):
        return "StringType"

    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int
        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String
        self.value = value



class Node():
    def __init__(self, var, reg, start_time, end_time, val):
        self.var = var
        self.reg = reg
        self.start_time = start_time
        self.end_time = end_time
        self.val = val
        self.adjacent_nodes = []
        self.color = None

    def add_edge(self, node):
        self.adjacent_nodes.append(node)
        
    def live_ranges(self):
        return self.end_time - self.start_time

class Graph:
    def __init__(self):
        self.nodes = []
        self.rules = []

    def add_node(self, var, reg, start_time, end_time, val):
        node = Node(var, reg, start_time, end_time, val)
        self.nodes.append(node)

    def add_edge(self, var1, var2):
        node1 = self.find_node_by_var(var1)
        node2 = self.find_node_by_var(var2)
        if self.check_overlap(node1, node2):
            node1.add_edge(node2)
            node2.add_edge(node1)

    def find_node_by_var(self, var):
        for node in self.nodes:
            if node.var == var:
                return node
        return None

    def check_overlap(self, node1, node2):
        return not(node1.end_time < node2.start_time or node2.end_time < node1.start_time)
        
    def sort_nodes(self):
        self.nodes.sort(key=lambda node: (node.var.count('_'), node.live_ranges()), reverse=True)

    def color_graph(self):
        colored = self.color_util(8)
        while not colored:
            self.rules.append({'data': [self.nodes[-1].var, self.nodes[-1].reg, self.nodes[-1].val]})
            self.nodes.pop()
            colored = self.color_util(8)

    def color_util(self, num_colors):
        for node in self.nodes:
            available_colors = set(range(1, num_colors + 1))
            for adj_node in node.adjacent_nodes:
                if adj_node.color in available_colors:
                    available_colors.remove(adj_node.color)
            if not available_colors:
                return False
            node.color = min(available_colors)
        return True
        
    def display(self):
        for node in self.nodes:
            adjacent_values = [adj_node.var for adj_node in node.adjacent_nodes]
            print(f"Node {node.var}: Adjacent Nodes {adjacent_values}, Color: {node.color}")
            
    def gen_rules(self):
        for node in self.nodes:
            self.rules.append({node.reg: 't' + str(node.color-1)})
        return self.rules
    

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File
        self.astTree = astTree
        self.env = env
        self.className = "ZCodeClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".asm")
        self.allVars = {}
        self.allStringVars = {}
        self.for_concat = 0
        self.register = {
            'f0': [], 'f1': [], 'f2': [], 'f3': [], 'f4': [], 'f5': [], 'f6': [], 'f7': [], 
            'f8': [], 'f9': [], 'f10': [], 'f11': [], 'f12': [], 'f13': [], 'f14': [], 'f15': [], 
            # 't0': [], 't1': [], 't2': [], 't3': [], 't4': [], 't5': [], 't6': [], 't7': [],
            # 's0': [], 's1': [], 's2': [], 's3': [], 's4': [], 's5': [], 's6': [], 's7': [],
            # 't8': [], 't9': [],
            # 'at': [], 
            # 'v0': [], 'v1': [],
            # 'a0': [], 'a1': [], 'a2': [], 'a3': [],
        }
        self.register_dest = []
        self.register_for_num = 0
        self.count = 0
        self.number_of_spill = 0
        self.need_to_reallocate = False
        self.rules = None

    def getFreeRegister(self):
        for key, value in self.register.items():
            if len(value) == 0:
                return key
        self.number_of_spill += 1
        result = 'SPILL' + str(self.number_of_spill)
        self.register.update({result: []})
        self.need_to_reallocate = True
        return result
    
    def getFreeRegisterForNumber(self, val):
        for key, value in self.register.items():
            if key not in self.register_dest and val in value:
                return key
            
        if self.register_dest != []:
            for key, value in self.register.items():
                if key not in self.register_dest:
                    self.register[key] = [item for item in value if not isinstance(item, (int, float))]

        for key, value in self.register.items():
            if len(value) == 0:
                return key
        self.number_of_spill += 1
        result = 'SPILL' + str(self.number_of_spill)
        self.register.update({result: []})
        self.need_to_reallocate = True
        return result
                 
    def getRegOfId(self, id, scope: str):
        # in scope first
        for key, value in self.allVars.items():
            if id == key and value[1] == scope:
                return value[0]
        # in global later
        for key, value in self.allVars.items():
            if id == key:
                return value[0]
        return
            
    def releaseRegisterForNumber(self, is_release_reg_dest: bool):
        if is_release_reg_dest:
            for key, value in self.register.items():
                self.register[key] = [item for item in value if not isinstance(item, (int, float))]
            self.register_dest = []
        else:
            for key, value in self.register.items():
                if key not in self.register_dest:
                    self.register[key] = [item for item in value if not isinstance(item, (int, float))]
        return
    
    def releaseRegisterInScope(self, scope: str):
        allRegsToRelease = []
        for key, value in self.allVars.items():
            if value[1] == scope:
                allRegsToRelease.append((key, value[0]))
        for reg in allRegsToRelease:
            if reg[0] in self.register[reg[1]]:
                self.register[reg[1]].remove(reg[0])

    # def releaseRegisterByName(self, register: str, id: str):
    #     if id in self.register[register]:
    #         self.register[register].remove(id)


    def printOut(self):
        print("All vars: ", end="")
        for key, value in self.allVars.items():
            print(f"{key} {value}, ", end="")
        print("\nAll registers: ", end="")
        for key, value in self.register.items():
            print(f"{key} {value}, ", end="")
        print("\nRegister Destination: ", self.register_dest)
        print('\n')


    def reallocate(self, allVars: dict):
        graph = Graph()
        for key, value in allVars.items():
            graph.add_node(key, value[0], value[2], value[3], int(value[4]))
        for i in range(0, len(graph.nodes)):
            for j in range(i+1, len(graph.nodes)):
                graph.add_edge(graph.nodes[i].var, graph.nodes[j].var)
                
        graph.sort_nodes()
        graph.color_graph()
        # graph.display()
        self.rules = graph.gen_rules()
        # print(self.rules)


    def allocate_string_data(self):
        for i in self.allStringVars:
            if self.allStringVars[i][1] != "_CONCAT":
                self.emit.emitPUSHSTRING(self.allStringVars[i][1], i)
            else:
                self.emit.emitPUSHBUFFER(i)

    def allocate_float_data(self):
        for i in self.allVars:
            self.emit.emitPUSHICONST(i, self.allVars[i][4])

    def visitProgram(self, ast, c):
        self.emit.printout(self.emit.IO())

        e = SubBody(None, self.env)
        for decl in ast.decl:
            if type(decl) is VarDecl:
                self.count += 1
                e.sym = [self.visit(decl, e)] + e.sym

        main = None
        for decl in ast.decl:
            if type(decl) is FuncDecl:
                if decl.name.name == 'main':
                    main = decl
                else:
                    e.sym = [self.visit(decl, e)] + e.sym

        e.sym = [self.visit(main, e)] + e.sym
        if self.need_to_reallocate == True:
            self.reallocate(self.allVars)
        self.allocate_string_data()
        self.allocate_float_data()
        self.emit.emitMIPS(self.rules)
        return c
        

    def visitFuncDecl(self, ast, o):
        subctxt = o
        frame = Frame(ast.name, None)

        self.emit.printout(self.emit.emitMETHOD(ast.name.name))

        self.emit.printout(self.emit.putSP())

        glenv = subctxt.sym
        body = ast.body

        for ele in body.stmt:
            self.count += 1
            glenv = [self.visit(ele, SubBody(frame, glenv))] + glenv

        self.releaseRegisterInScope(ast.name.name)
        self.emit.printout(self.emit.returnSP())
        if ast.name.name == "main":
            self.emit.printout("	jal exit\n")
        else:
            self.emit.printout("	jr $ra")
        return SubBody(None, [Symbol(ast.name, MType(list(), None), CName(self.className))] + subctxt.sym)
        
    
    def visitVarDecl(self, ast, c):
        varName = ast.name.name
        varInit = ast.varInit
        varType = ast.varType

        if c.frame is None:
            # Global scope
            register = self.getFreeRegister()
            self.allVars.update({varName: [register, 'GLOBAL', self.count, self.count, varInit.value]})
            self.register[register].append(varName)

            val = CName(self.className)
            self.emit.printout(self.emit.emitATTRIBUTE(register, varInit.value, False))
        else:
            register = self.getFreeRegister()
            val = CName(c.frame.name.name)

            if type(varInit) is not NumberLiteral:
                value = self.visit(varInit, c)
                if value[0] == "IO":
                    # cai IO dang nam o v0, nen bay gio load vao cai cho register la duoc
                    self.emit.printout(self.emit.emitATTRIBUTE_MOVE(register, "$v0", True))
                elif type(value[1]) is StringType:
                    if type(varInit) is StringLiteral:
                        self.allStringVars.update({varName: [c.frame.name.name, self.allStringVars[value[2]]][1]})
                    else:
                        self.allStringVars.update({varName: [c.frame.name.name, "_CONCAT"]})
                        self.emit.printout(f"    la $t2, {varName}\n")
                        self.emit.printout(value[0])
                        # c = a ... b
                elif type(value[1]) is BoolType:
                    self.allVars.update({varName: [register, c.frame.name.name, self.count, self.count, varInit.value]})
                    self.register[register].append(varName)
                    self.emit.printout(self.emit.emitATTRIBUTE(register, varName, True))
            else:
                self.allVars.update({varName: [register, c.frame.name.name, self.count, self.count, varInit.value]})
                self.register[register].append(varName)
                self.emit.printout(self.emit.emitATTRIBUTE(register, varName, True))
            
        return Symbol(varName, varType, val)

    def visitCallStmt(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        in_ = ("", list(), "")
        for x in ast.args:
            str1, typ1, reg1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1), in_[2] + reg1)

        if ast.name.name == 'writeNumber':
            self.emit.printout(self.emit.emitLOADSYSCALL(in_[2]))
        elif ast.name.name == "writeString":
            self.emit.printout(self.emit.emitLOADSYSCALL_PRINTSTRING(in_[2], in_[0]))
        elif ast.name.name == "writeBool":
            self.emit.printout(self.emit.emitLOADSYSCALL_PRINTBOOL(in_[2]))
        self.emit.printout(self.emit.emitINVOKEFUNCTION(ast.name.name))
        
        self.releaseRegisterForNumber(True)
        # self.releaseRegisterInScope(frame.name.name)
        # self.releaseRegisterByName(in_[2], ast.name.name)
        # self.printOut()
        
    def visitCallExpr(self, ast, o):
        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym

        in_ = ("", list(), "")
        for x in ast.args:
            str1, typ1, reg1 = self.visit(x, Access(frame, nenv, False, True))
            in_ = (in_[0] + str1, in_[1].append(typ1), in_[2] + reg1)

        if ast.name.name == 'readNumber':
            pass
        self.emit.printout(self.emit.emitINVOKEFUNCTION(ast.name.name))
        self.releaseRegisterForNumber(True)
        return "IO", "IO", "IO"


    def visitId(self, ast, c):
        # neu la string
        if ast.name in self.allStringVars:
            reg = "t0" if self.for_concat == 0 else "t1"
            self.for_concat += 1
            if self.for_concat == 2:
                self.for_concat = 0
            return self.emit.emitGETSTRINGATTRIBUTE(reg, ast.name), StringType(), ast.name
        
        sym = next(filter(lambda x: x.name == ast.name, c.sym))
        name = sym.name
        register = self.getRegOfId(name, c.frame.name.name)
        if register:
            # ve phai thi khong can lam gi het, chi can lay register
            self.allVars[name][3] = self.count
            if type(sym.mtype) is BoolType:
                res = "_TRUE" if self.allVars[ast.name][4] == True else "_FALSE"
                return ast.name, sym.mtype, res
            else:
                return self.emit.emitGETATTRIBUTE("", c.frame), sym.mtype, register
        # ve trai thi phai luu register
        return self.emit.emitGETATTRIBUTE(register, c.frame), sym.mtype


    def visitNumberLiteral(self, ast, o):
        register = self.getFreeRegisterForNumber(ast.value)
        self.register[register].append(ast.value)
        # t = any([register, o.frame.name.name, self.count, self.count, 0] == value for _, value in self.allVars.items())
        t = any([register, o.frame.name.name, self.count, self.count, ast.value] == value for _, value in self.allVars.items())
        if not t:
            self.register_for_num += 1
            string = '_' * self.register_for_num
            self.allVars[string] = [register, o.frame.name.name, self.count, self.count, 0]
            self.allVars[string] = [register, o.frame.name.name, self.count, self.count, ast.value]
        return self.emit.emitCONST(register, string), NumberType(), register
        # return string, NumberType(), register

    def visitStringLiteral(self, ast, c):
        string = '_' * len(self.allStringVars) + "STRING"
        self.allStringVars.update({string: [c.frame.name.name, ast.value]})
        reg = "t0" if self.for_concat == 0 else "t1"
        self.for_concat += 1
        if self.for_concat == 2:
            self.for_concat = 0
        return self.emit.emitGETSTRINGATTRIBUTE(reg, string), StringType(), string
    
    def visitBooleanLiteral(self, ast, c):
        name = "_TRUE" if ast.value == True else "_FALSE"
        res = "True" if ast.value == True else "False"
        return name, BoolType(), res

    def visitBinaryOp(self, ast, c):
        self.releaseRegisterForNumber(False)

        reg1 = reg2 = ""
        flag = False
        access = Access(c.frame, c.sym, False, True)

        lCode, lType, lReg = self.visit(ast.left, access)

        if type(lType) is not StringType:
            for item in self.register[lReg]:
                if isinstance(item, (int, float)):
                    if lReg not in self.register_dest:
                        self.register_dest.append(lReg)
                    flag = True

            rCode, rType, rReg = self.visit(ast.right, access)
            for item in self.register[rReg]:
                if isinstance(item, (int, float)):
                    if flag == False:
                        if rReg not in self.register_dest:
                            self.register_dest.append(rReg)
                        reg1, reg2 = rReg, lReg
                        
            if flag == True:
                reg1, reg2 = lReg, rReg

            if reg1 == "":
                reg1, reg2 = lReg, rReg
                temp = self.getFreeRegister()

                t = any([temp, c.frame.name.name, self.count, self.count, 0] == value for _, value in self.allVars.items())
                if not t:
                    self.register_for_num += 1
                    string = '_' * self.register_for_num
                    self.allVars[string] = [temp, c.frame.name.name, self.count, self.count, 0]

                if temp not in self.register_dest:
                    self.register_dest.append(temp)
                self.register[self.register_dest[-1]].append(0)
            
            if reg1 in self.register_dest and reg2 in self.register_dest:
                self.register_dest.remove(reg1)
                self.register_dest.remove(reg2)
                self.register_dest.append(reg1)
            if ast.op == '+':
                return lCode + rCode + self.emit.emitADDOP(reg1, reg2, self.register_dest[-1], NumberType()), NumberType(), self.register_dest[-1]
            elif ast.op == '-':
                return lCode + rCode + self.emit.emitSUBOP(reg1, reg2, self.register_dest[-1], NumberType()), NumberType(), self.register_dest[-1]
            elif ast.op == '*':
                return lCode + rCode + self.emit.emitMULOP(reg1, reg2, self.register_dest[-1], NumberType()), NumberType(), self.register_dest[-1]
            # elif ast.op == '<':
            #     return lCode + rCode + self.emit.emitMULOP(reg1, reg2, "self.register_dest[-1]", NumberType()), NumberType(), self.register_dest[-1]
        else:
            rCode, rType, rReg = self.visit(ast.right, access)

            string = '_' * len(self.allStringVars) + "STRING"
            self.allStringVars.update({string: [c.frame.name.name, "_CONCAT"]})

            return lCode + rCode + "    jal concat\n", StringType(), string

    def visitUnaryOp(self, ast, c):
        self.releaseRegisterForNumber(False)

        reg1 = ""
        flag = False
        access = Access(c.frame, c.sym, False, True)

        opCode, opType, opReg = self.visit(ast.operand, access)

        for item in self.register[opReg]:
            if isinstance(item, (int, float)):
                if opReg not in self.register_dest:
                    self.register_dest.append(opReg)
                flag = True
  
        if flag == True:
            reg1 = opReg

        if reg1 == "":
            reg1 = opReg
            temp = self.getFreeRegister()

            t = any([temp, c.frame.name.name, self.count, self.count, 0] == value for _, value in self.allVars.items())
            if not t:
                self.register_for_num += 1
                string = '_' * self.register_for_num
                self.allVars[string] = [temp, c.frame.name.name, self.count, self.count, 0]

            if temp not in self.register_dest:
                self.register_dest.append(temp)
            self.register[self.register_dest[-1]].append(0)
        
        if reg1 in self.register_dest:
            self.register_dest.remove(reg1)
            self.register_dest.append(reg1)

        if ast.op == '-':
            return opCode + self.emit.emitNEGOP(reg1, self.register_dest[-1], NumberType()), NumberType(), self.register_dest[-1]
        elif ast.op == 'not':
            return opCode + self.emit.emitMULOP(reg1, self.register_dest[-1], NumberType()), NumberType(), self.register_dest[-1]
        
    # def visitIf(self, ast, c):


