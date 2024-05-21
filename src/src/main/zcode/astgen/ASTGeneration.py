from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
from functools import reduce

class ASTGeneration(ZCodeVisitor):

# program: nullable_newline_list decl_list EOF;
# decl_list: decl decl_list | decl;
# decl: var_decl | func_decl;
    
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.decl_list()))
    
    def visitDecl_list(self,ctx:ZCodeParser.Decl_listContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.decl())] + self.visit(ctx.decl_list())
        return [self.visit(ctx.decl())]
    
    def visitDecl(self,ctx:ZCodeParser.DeclContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        return self.visit(ctx.func_decl())
    
# var_decl: var_decl_part newline_list;
# var_decl_part: optional_vardecl | must_vardecl | arr_decl;
# optional_vardecl: (scalar_type | DYNAMIC) IDENTIFIER optional_initialize;
# must_vardecl: VAR IDENTIFIER initialize;

    def visitVar_decl(self,ctx:ZCodeParser.Var_declContext):
        return self.visit(ctx.var_decl_part())

    def visitVar_decl_part(self,ctx:ZCodeParser.Var_decl_partContext):
        if ctx.optional_vardecl():
            return self.visit(ctx.optional_vardecl())
        elif ctx.must_vardecl():
            return self.visit(ctx.must_vardecl())
        return self.visit(ctx.arr_decl())

    def visitOptional_vardecl(self,ctx:ZCodeParser.Optional_vardeclContext):
        if ctx.scalar_type():
            name = Id(ctx.IDENTIFIER().getText())
            typee = self.visit(ctx.scalar_type())
            initialize = self.visit(ctx.optional_initialize())
            return VarDecl(name, typee, None, initialize)
        else:
            name = Id(ctx.IDENTIFIER().getText())
            modifier = ctx.DYNAMIC().getText()
            initialize = self.visit(ctx.optional_initialize())
            return VarDecl(name, None, modifier, initialize)

    def visitMust_vardecl(self,ctx:ZCodeParser.Must_vardeclContext):
        name = Id(ctx.IDENTIFIER().getText())
        modifier = ctx.VAR().getText()
        initialize = self.visit(ctx.initialize())
        return VarDecl(name, None, modifier, initialize)
    
# arr_decl: scalar_type IDENTIFIER arr_size_list optional_initialize;
# arr_size_list: LS arr_size_prime RS;
# arr_size_prime: NUMBERLIT | arr_size_prime COMMA NUMBERLIT;
# scalar_type: NUMBER | BOOL | STRING;
# optional_initialize: initialize | ;
# initialize: ASSIGN expr;
    
    def visitArr_decl(self,ctx:ZCodeParser.Arr_declContext):
        eleType = self.visit(ctx.scalar_type())
        size = self.visit(ctx.arr_size_list())
        varInit = self.visit(ctx.optional_initialize())
        arrayType = ArrayType(size, eleType)
        name = Id(ctx.IDENTIFIER().getText())
        return VarDecl(name, arrayType, None, varInit)

    def visitArr_size_list(self,ctx:ZCodeParser.Arr_size_listContext):
        return self.visit(ctx.arr_size_prime())

    def visitArr_size_prime(self,ctx:ZCodeParser.Arr_size_primeContext):
        if ctx.COMMA():
            return self.visit(ctx.arr_size_prime()) + [float(ctx.NUMBERLIT().getText())]
        return [float(ctx.NUMBERLIT().getText())]

    def visitScalar_type(self,ctx:ZCodeParser.Scalar_typeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()

    def visitOptional_initialize(self,ctx:ZCodeParser.Optional_initializeContext):
        return self.visit(ctx.initialize()) if ctx.initialize() else None
    
    def visitInitialize(self,ctx:ZCodeParser.InitializeContext):
        return self.visit(ctx.expr())
    

    # func_decl: FUNC IDENTIFIER param_decl endfunc;
    # param_decl: LP param_list RP;
    # param_list: param_prime |;
    # param_prime: param COMMA param_prime | param;

    def visitFunc_decl(self,ctx:ZCodeParser.Func_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = self.visit(ctx.param_decl())
        body = self.visit(ctx.endfunc())
        return FuncDecl(name, param, body)
    
    def visitParam_decl(self,ctx:ZCodeParser.Param_declContext):
        return self.visit(ctx.param_list())
    
    def visitParam_list(self,ctx:ZCodeParser.Param_listContext):
        return self.visit(ctx.param_prime()) if ctx.param_prime() else []
    
    def visitParam_prime(self,ctx:ZCodeParser.Param_primeContext):
        if ctx.COMMA():
            return [self.visit(ctx.param())] + self.visit(ctx.param_prime())
        return [self.visit(ctx.param())]
    
    # param: scalar_type param_name;
    # param_name: IDENTIFIER | IDENTIFIER arr_size_list;
    # endfunc: nullable_newline_list blockstmt | nullable_newline_list returnstmt newline_list | newline_list;

    def visitParam(self,ctx:ZCodeParser.ParamContext):
        typee = self.visit(ctx.scalar_type())
        temp = self.visit(ctx.param_name())
        if (temp[1] != []):
            arrayType = ArrayType(temp[1], typee)
            return VarDecl(temp[0], arrayType, None, None)
        else:
            return VarDecl(temp[0], typee, None, None)
    
    def visitParam_name(self,ctx:ZCodeParser.Param_nameContext):
        if ctx.getChildCount() == 1:
            return (Id(ctx.IDENTIFIER().getText()), [])
        else:
            return (Id(ctx.IDENTIFIER().getText()), self.visit(ctx.arr_size_list()))
    
    def visitEndfunc(self,ctx:ZCodeParser.EndfuncContext):
        if ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        return None

# assignstmt: lhs ASSIGN expr;
# lhs: IDENTIFIER | (IDENTIFIER LS index_operators RS);

    def visitAssignstmt(self,ctx:ZCodeParser.AssignstmtContext):
        return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))
    
    def visitLhs(self,ctx:ZCodeParser.LhsContext):
        if ctx.getChildCount() > 1:
            arr = Id(ctx.IDENTIFIER().getText())
            idx = self.visit(ctx.index_operators())
            return ArrayCell(arr, idx)
        return Id(ctx.IDENTIFIER().getText())
    
    def visitLiteral(self,ctx:ZCodeParser.LiteralContext):
        if ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(ctx.BOOLLIT().getText() == 'true')
        elif ctx.STRINGLIT():
            return StringLiteral(str(ctx.STRINGLIT().getText()))
    
# expr: expr1;
# expr1: expr2 CONCAT expr2 | expr2;
# expr2: expr3 RELOP expr3 | expr3;
# expr3: expr3 (AND | OR) expr4 | expr4;
# expr4: expr4 (ADD | SUB) expr5 | expr5;
# expr5: expr5 (MUL | DIV | MOD) expr6 | expr6;
# expr6: NOT expr6 | expr7;
# expr7: SUB expr7 | expr8;
# expr8: LS (index_operators | ) RS | index_operation | expr9;
# expr9: LP expr RP | literal | IDENTIFIER | callstmt;

    def visitExpr(self,ctx:ZCodeParser.ExprContext):
        if ctx.expr1():
            return self.visit(ctx.expr1())
        return None
    
    def visitExpr1(self,ctx:ZCodeParser.Expr1Context):
        if ctx.CONCAT():
            return BinaryOp(ctx.CONCAT().getText(), self.visit(ctx.expr2(0)), self.visit(ctx.expr2(1)))
        return self.visit(ctx.expr2(0))
    
    def visitExpr2(self,ctx:ZCodeParser.Expr2Context):
        if ctx.RELOP():
            return BinaryOp(ctx.RELOP().getText(), self.visit(ctx.expr3(0)), self.visit(ctx.expr3(1)))
        return self.visit(ctx.expr3(0))
    
    def visitExpr3(self,ctx:ZCodeParser.Expr3Context):
        if ctx.expr3():
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr3()), self.visit(ctx.expr4()))
        return self.visit(ctx.expr4())
    
    def visitExpr4(self,ctx:ZCodeParser.Expr4Context):
        if ctx.expr4():
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr4()), self.visit(ctx.expr5()))
        return self.visit(ctx.expr5())
    
    def visitExpr5(self,ctx:ZCodeParser.Expr5Context):
        if ctx.expr5():
            return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.expr5()), self.visit(ctx.expr6()))
        return self.visit(ctx.expr6())
    
    def visitExpr6(self,ctx:ZCodeParser.Expr6Context):
        if ctx.expr6():
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr6()))
        return self.visit(ctx.expr7())
    
    def visitExpr7(self,ctx:ZCodeParser.Expr7Context):
        if ctx.expr7():
            return UnaryOp(ctx.getChild(0).getText(), self.visit(ctx.expr7()))
        return self.visit(ctx.expr8())
    
    def visitExpr8(self,ctx:ZCodeParser.Expr8Context):
        if ctx.index_operators():
            return ArrayLiteral(self.visit(ctx.index_operators()))
        elif ctx.expr9():
            return self.visit(ctx.expr9())
        elif ctx.index_operation():
            return self.visit(ctx.index_operation())
        return ArrayLiteral([])
    
    def visitExpr9(self,ctx:ZCodeParser.Expr9Context):
        if ctx.expr():
            return self.visit(ctx.expr())
        elif ctx.literal():
            return self.visit(ctx.literal())
        elif ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        elif ctx.callstmt():
            callstmt = self.visit(ctx.callstmt())
            name = callstmt.name
            args = callstmt.args
            return CallExpr(name, args)
    

    # index_operation: expr9 LS index_operators RS;
    # index_operators: expr | expr COMMA index_operators;
    
    def visitIndex_operation(self,ctx:ZCodeParser.Index_operationContext):
        arr = self.visit(ctx.expr9())
        idx = self.visit(ctx.index_operators())
        return ArrayCell(arr, idx)
    
    def visitIndex_operators(self,ctx:ZCodeParser.Index_operatorsContext):
        if ctx.COMMA():
            return [self.visit(ctx.expr())] + self.visit(ctx.index_operators())
        return [self.visit(ctx.expr())]
    

# ifstmt: IF cond_block optional_elif_list | IF cond_block optional_elif_list optional_else;
# cond_block: LP expr RP nullable_newline_list stmt;
# optional_elif_list: optional_elif | ;
# optional_elif: ELIF cond_block optional_elif | ELIF cond_block;
# optional_else: ELSE stmt;
    
    def visitIfstmt(self,ctx:ZCodeParser.IfstmtContext):
        if (ctx.optional_else()):
            expr = self.visit(ctx.cond_block())[0]
            thenStmt = self.visit(ctx.cond_block())[1]
            elifStmt = self.visit(ctx.optional_elif_list())
            elseStmt = self.visit(ctx.optional_else())
            return If(expr, thenStmt, elifStmt, elseStmt)
        else:
            expr = self.visit(ctx.cond_block())[0]
            thenStmt = self.visit(ctx.cond_block())[1]
            elifStmt = self.visit(ctx.optional_elif_list())
            return If(expr, thenStmt, elifStmt, None)
    
    def visitCond_block(self,ctx:ZCodeParser.Cond_blockContext):
        expr = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        return (expr, stmt)
    
    def visitOptional_elif_list(self,ctx:ZCodeParser.Optional_elif_listContext):
        if ctx.optional_elif():
            return self.visit(ctx.optional_elif())
        return []
    
    def visitOptional_elif(self,ctx:ZCodeParser.Optional_elifContext):
        if ctx.optional_elif():
            return [self.visit(ctx.cond_block())] + self.visit(ctx.optional_elif())
        return [self.visit(ctx.cond_block())]
    
    def visitOptional_else(self,ctx:ZCodeParser.Optional_elseContext):
        if ctx.stmt():
            return self.visit(ctx.stmt())
        return None
    
    # forstmt: FOR IDENTIFIER UNTIL expr BY expr nullable_newline_list stmt;
    def visitForstmt(self,ctx:ZCodeParser.ForstmtContext):
        name = ctx.IDENTIFIER().getText()
        condExpr = self.visit(ctx.expr(0))
        updExpr = self.visit(ctx.expr(1))
        body = self.visit(ctx.stmt())
        return For(Id(name), condExpr, updExpr, body)
    
    def visitBreakstmt(self,ctx:ZCodeParser.BreakstmtContext):
        return Break()
    
    def visitContinuestmt(self,ctx:ZCodeParser.ContinuestmtContext):
        return Continue()
    
    def visitReturnstmt(self,ctx:ZCodeParser.ReturnstmtContext):
        return Return(ctx.expr().accept(self)) if ctx.expr() else Return(None)
    
# callstmt: IDENTIFIER paramcall_part;
# paramcall_part: LP paramcall_list RP;
# paramcall_list: paramcall_prime |;
# paramcall_prime: paramcall COMMA paramcall_prime | paramcall;
# paramcall: expr | IDENTIFIER | IDENTIFIER paramcall;

    def visitCallstmt(self,ctx:ZCodeParser.CallstmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        args = self.visit(ctx.paramcall_part())
        return CallStmt(name, args)
    
    def visitParamcall_part(self,ctx:ZCodeParser.Paramcall_partContext):
        return self.visit(ctx.paramcall_list())
    
    def visitParamcall_list(self,ctx:ZCodeParser.Paramcall_listContext):
        return self.visit(ctx.paramcall_prime()) if ctx.paramcall_prime() else []
    
    def visitParamcall_prime(self,ctx:ZCodeParser.Paramcall_primeContext):
        if ctx.COMMA():
            return self.visit(ctx.paramcall()) + self.visit(ctx.paramcall_prime())
        return self.visit(ctx.paramcall())
    
    def visitParamcall(self,ctx:ZCodeParser.ParamcallContext):
        if ctx.paramcall():
            return [Id(ctx.IDENTIFIER().getText())] + self.visit(ctx.paramcall())
        elif ctx.expr():
            return [self.visit(ctx.expr())]
        return [Id(ctx.IDENTIFIER().getText())]
    
    # blockstmt: BEGIN newline_list stmt_list END newline_list;
    def visitBlockstmt(self,ctx:ZCodeParser.BlockstmtContext):
        return Block(self.visit(ctx.stmt_list()))
    
# stmt_list: stmt_prime |;
# stmt_prime: stmt stmt_prime | stmt;
    
    def visitStmt_list(self,ctx:ZCodeParser.Stmt_listContext):
        return self.visit(ctx.stmt_prime()) if ctx.stmt_prime() else []
    
    def visitStmt_prime(self,ctx:ZCodeParser.Stmt_primeContext):
        if ctx.stmt_prime():
            return [self.visit(ctx.stmt())] + self.visit(ctx.stmt_prime())
        return [self.visit(ctx.stmt())]
    
# stmt: assignstmt newline_list
#      | ifstmt 
#      | forstmt
#      | breakstmt newline_list
#      | continuestmt newline_list
#      | callstmt newline_list
#      | blockstmt
#      | returnstmt newline_list
#      | var_decl
#     ;
    
    def visitStmt(self,ctx:ZCodeParser.StmtContext):
        if ctx.assignstmt():
            return self.visit(ctx.assignstmt())
        elif ctx.ifstmt():
            return self.visit(ctx.ifstmt())
        elif ctx.forstmt():
            return self.visit(ctx.forstmt())
        elif ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        elif ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        elif ctx.callstmt():
            return self.visit(ctx.callstmt())
        elif ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        elif ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        else:
            return self.visit(ctx.var_decl())
    

