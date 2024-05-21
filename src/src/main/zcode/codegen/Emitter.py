from Utils import *
from StaticCheck import *
from StaticError import *
import CodeGenerator as cgen
from MachineCode import MipsCode



class Emitter():
    def __init__(self, filename):
        self.filename = filename
        self.buff = list()
        self.mips = MipsCode()

    def emitATTRIBUTE(self, register, value=None, indent=True):
        return self.mips.emitATTRIBUTE(register, value, indent)
    
    def emitATTRIBUTE_MOVE(self, register, register2=None, indent=True):
        return self.mips.emitATTRIBUTE_MOVE(register, register2, indent)
    
    def emitGETATTRIBUTE(self, register, frame):
        if register == "":
            return ""
        self.buff.append(self.mips.emitGETATTRIBUTE(register))
        return self.mips.emitGETATTRIBUTE(register)
    
    def emitGETSTRINGATTRIBUTE(self, register, name):
        # self.buff.append(self.mips.emitGETSTRINGATTRIBUTE(register, name))
        return self.mips.emitGETSTRINGATTRIBUTE(register, name)

    def emitPUSHICONST(self, name, in_):
        self.buff.append(self.mips.emitICONST(name, float(in_)))
        return self.mips.emitICONST(name, float(in_))
    
    def emitCONST(self, register, name):
        self.buff.append(self.mips.emitCONST(register, name))
        return self.mips.emitCONST(register, name)
    
    def emitPUSHSTRING(self, in_, var):
        self.buff.append(self.mips.emitSTRING(in_, var))
        return self.mips.emitSTRING(in_, var)
    
    def emitPUSHBUFFER(self, var):
        self.buff.append(self.mips.emitBUFFER(var))
        return self.mips.emitBUFFER(var)

    def emitINVOKEFUNCTION(self, lexeme):
        return self.mips.emitINVOKEFUNCTION(lexeme)
    
    def emitLOADSYSCALL(self, reg_des):
        return self.mips.emitLOADSYSCALL(reg_des)
    
    def emitLOADSYSCALL_PRINTSTRING(self, var, temp):
        if "_" in temp:
            self.buff.append(f"    la $t2, {var}\n")
            self.buff.append(temp)
        return self.mips.emitLOADSYSCALL_PRINTSTRING(var)
    
    def emitLOADSYSCALL_PRINTBOOL(self, var):
        return self.mips.emitLOADSYSCALL_PRINTBOOL(var)


    def emitADDOP(self, register1, register2, des_register, in_):
        if type(in_) is NumberType:
            self.buff.append(self.mips.emitIADD(register1, register2, des_register))
            return self.mips.emitIADD(register1, register2, des_register)
        
    def emitSUBOP(self, register1, register2, des_register, in_):
        if type(in_) is NumberType:
            self.buff.append(self.mips.emitISUB(register1, register2, des_register))
            return self.mips.emitISUB(register1, register2, des_register)
        
    def emitMULOP(self, register1, register2, des_register, in_):
        if type(in_) is NumberType:
            self.buff.append(self.mips.emitIMUL(register1, register2, des_register))
            return self.mips.emitIMUL(register1, register2, des_register)
        
    def emitNEGOP(self, register1, des_register, in_):
        if type(in_) is NumberType:
            self.buff.append(self.mips.emitINEG(register1, des_register))
            return self.mips.emitINEG(register1, des_register)
        
    # def emitRELOP(self, register1, register2, des_register, in_):
    #     if type(in_) is NumberType:
    #         self.buff.append(self.mips.emitRELOP(register1, register2, "des_register"))
    #         return self.mips.emitRELOP(register1, register2, "des_register")


    def emitMETHOD(self, lexeme):
        return self.mips.emitMETHOD(lexeme)
    
    def putSP(self):
        return "    addi $sp, $sp, -4\n" + "    sw $ra, 0($sp)\n"

    def returnSP(self):
        return "    lw $ra, 0($sp)\n" + "    addi $sp, $sp, 4\n"

    def emitENDMETHOD(self, frame):
        buffer = list()
        return ''.join(buffer)


    def emitMIPS(self, rules):
        file = open(self.filename, "w")
        if rules != None:
            file.write(".data\n")
            for rule in rules:
                if 'data' in rule:
                    data = rule['data']
                    file.write(f"   {data[0]}: .word {data[2]}\n")
            file.write("\n.text\n")
            for line in self.buff:
                tokens = line.split()
                lineFlag = False
                for i in range(len(tokens)):
                    flag = False
                    for rule in rules:
                        for key, value in rule.items():
                            if key == 'data':
                                if tokens[i] == "li":
                                    if value[1] in tokens[i+1]:
                                        tokens[i] = '#' + tokens[i]
                                        flag = True
                                        lineFlag = True
                                elif value[1] in tokens[i]:
                                    newline = MipsCode.INDENT + "lw " + "$t8, " + rule[key][0] + '\n'
                                    file.write(newline)
                                    tokens[i] = tokens[i].replace(rule[key][1], "t8")
                                    flag = True
                            else: 
                                if key in tokens[i]:
                                    tokens[i] = tokens[i].replace(key, value)
                                    flag = True
                        if flag == True:
                            break
                    if lineFlag == True:
                        break

                file.write(MipsCode.INDENT + ' '.join(tokens) + '\n')
        else:
            file.write(''.join(self.buff))
        file.close()

    ''' print out the code to screen
    *   @param in the code to be printed out
    '''
    def printout(self, in_):
        #in_: String

        self.buff.append(in_)

    def clearBuff(self):
        self.buff.clear()

    def IO(self) -> str:
        string = """
    .globl readNumber
    .globl writeNumber
    .globl writeString
    .globl exit
    .globl main
    .data
_TRUE:  .asciiz "true"
_FALSE: .asciiz "false"
    .text

j main

concat:
    copy_loop_a:
        lb $t3, 0($t0)
        beqz $t3, copy_loop_b
        sb $t3, 0($t2)
        addi $t0, $t0, 1
        addi $t2, $t2, 1 
        j copy_loop_a
    copy_loop_b:
        lb $t3, 0($t1)
        beqz $t3, end
        sb $t3, 0($t2)
        addi $t1, $t1, 1
        addi $t2, $t2, 1
        j copy_loop_b
    end:
        sb $zero, 0($t2)
        jr $ra

readNumber:
    li $v0, 5
    syscall
    jr $ra

writeNumber:
    li $v0, 2
    syscall
    jr $ra

writeBool:
	li $v0, 4
    syscall
    jr $ra

writeString:
	li $v0, 4
    syscall
    jr $ra

exit:
    li $v0, 10
    syscall
"""
        return string





        
