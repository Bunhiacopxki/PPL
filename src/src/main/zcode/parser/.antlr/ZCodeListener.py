# Generated from c://Users//hp450//Desktop//PPL_extra//doing//src//main//zcode//parser//ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl_list.
    def enterDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl_list.
    def exitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_decl.
    def enterVar_decl(self, ctx:ZCodeParser.Var_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_decl.
    def exitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_decl_part.
    def enterVar_decl_part(self, ctx:ZCodeParser.Var_decl_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_decl_part.
    def exitVar_decl_part(self, ctx:ZCodeParser.Var_decl_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_vardecl.
    def enterOptional_vardecl(self, ctx:ZCodeParser.Optional_vardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_vardecl.
    def exitOptional_vardecl(self, ctx:ZCodeParser.Optional_vardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#must_vardecl.
    def enterMust_vardecl(self, ctx:ZCodeParser.Must_vardeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#must_vardecl.
    def exitMust_vardecl(self, ctx:ZCodeParser.Must_vardeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr_decl.
    def enterArr_decl(self, ctx:ZCodeParser.Arr_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr_decl.
    def exitArr_decl(self, ctx:ZCodeParser.Arr_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr_size_list.
    def enterArr_size_list(self, ctx:ZCodeParser.Arr_size_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr_size_list.
    def exitArr_size_list(self, ctx:ZCodeParser.Arr_size_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#arr_size_prime.
    def enterArr_size_prime(self, ctx:ZCodeParser.Arr_size_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#arr_size_prime.
    def exitArr_size_prime(self, ctx:ZCodeParser.Arr_size_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#scalar_type.
    def enterScalar_type(self, ctx:ZCodeParser.Scalar_typeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#scalar_type.
    def exitScalar_type(self, ctx:ZCodeParser.Scalar_typeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_initialize.
    def enterOptional_initialize(self, ctx:ZCodeParser.Optional_initializeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_initialize.
    def exitOptional_initialize(self, ctx:ZCodeParser.Optional_initializeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#initialize.
    def enterInitialize(self, ctx:ZCodeParser.InitializeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#initialize.
    def exitInitialize(self, ctx:ZCodeParser.InitializeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_decl.
    def enterFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_decl.
    def exitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_decl.
    def enterParam_decl(self, ctx:ZCodeParser.Param_declContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_decl.
    def exitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_list.
    def enterParam_list(self, ctx:ZCodeParser.Param_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_list.
    def exitParam_list(self, ctx:ZCodeParser.Param_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_prime.
    def enterParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_prime.
    def exitParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_name.
    def enterParam_name(self, ctx:ZCodeParser.Param_nameContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_name.
    def exitParam_name(self, ctx:ZCodeParser.Param_nameContext):
        pass


    # Enter a parse tree produced by ZCodeParser#endfunc.
    def enterEndfunc(self, ctx:ZCodeParser.EndfuncContext):
        pass

    # Exit a parse tree produced by ZCodeParser#endfunc.
    def exitEndfunc(self, ctx:ZCodeParser.EndfuncContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assignstmt.
    def enterAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assignstmt.
    def exitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lhs.
    def enterLhs(self, ctx:ZCodeParser.LhsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lhs.
    def exitLhs(self, ctx:ZCodeParser.LhsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr.
    def enterExpr(self, ctx:ZCodeParser.ExprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expr.
    def exitExpr(self, ctx:ZCodeParser.ExprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expr1.
    def enterExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr1.
    def exitExpr1(self, ctx:ZCodeParser.Expr1Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr2.
    def enterExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr2.
    def exitExpr2(self, ctx:ZCodeParser.Expr2Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr3.
    def enterExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr3.
    def exitExpr3(self, ctx:ZCodeParser.Expr3Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr4.
    def enterExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr4.
    def exitExpr4(self, ctx:ZCodeParser.Expr4Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr5.
    def enterExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr5.
    def exitExpr5(self, ctx:ZCodeParser.Expr5Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr6.
    def enterExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr6.
    def exitExpr6(self, ctx:ZCodeParser.Expr6Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr7.
    def enterExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr7.
    def exitExpr7(self, ctx:ZCodeParser.Expr7Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr8.
    def enterExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr8.
    def exitExpr8(self, ctx:ZCodeParser.Expr8Context):
        pass


    # Enter a parse tree produced by ZCodeParser#expr9.
    def enterExpr9(self, ctx:ZCodeParser.Expr9Context):
        pass

    # Exit a parse tree produced by ZCodeParser#expr9.
    def exitExpr9(self, ctx:ZCodeParser.Expr9Context):
        pass


    # Enter a parse tree produced by ZCodeParser#index_operation.
    def enterIndex_operation(self, ctx:ZCodeParser.Index_operationContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_operation.
    def exitIndex_operation(self, ctx:ZCodeParser.Index_operationContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_operators.
    def enterIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_operators.
    def exitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#ifstmt.
    def enterIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#ifstmt.
    def exitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#cond_block.
    def enterCond_block(self, ctx:ZCodeParser.Cond_blockContext):
        pass

    # Exit a parse tree produced by ZCodeParser#cond_block.
    def exitCond_block(self, ctx:ZCodeParser.Cond_blockContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_elif_list.
    def enterOptional_elif_list(self, ctx:ZCodeParser.Optional_elif_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_elif_list.
    def exitOptional_elif_list(self, ctx:ZCodeParser.Optional_elif_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_elif.
    def enterOptional_elif(self, ctx:ZCodeParser.Optional_elifContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_elif.
    def exitOptional_elif(self, ctx:ZCodeParser.Optional_elifContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_else.
    def enterOptional_else(self, ctx:ZCodeParser.Optional_elseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_else.
    def exitOptional_else(self, ctx:ZCodeParser.Optional_elseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forstmt.
    def enterForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forstmt.
    def exitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#breakstmt.
    def enterBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#breakstmt.
    def exitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continuestmt.
    def enterContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continuestmt.
    def exitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#returnstmt.
    def enterReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#returnstmt.
    def exitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#callstmt.
    def enterCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#callstmt.
    def exitCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramcall_part.
    def enterParamcall_part(self, ctx:ZCodeParser.Paramcall_partContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramcall_part.
    def exitParamcall_part(self, ctx:ZCodeParser.Paramcall_partContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramcall_list.
    def enterParamcall_list(self, ctx:ZCodeParser.Paramcall_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramcall_list.
    def exitParamcall_list(self, ctx:ZCodeParser.Paramcall_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramcall_prime.
    def enterParamcall_prime(self, ctx:ZCodeParser.Paramcall_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramcall_prime.
    def exitParamcall_prime(self, ctx:ZCodeParser.Paramcall_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#paramcall.
    def enterParamcall(self, ctx:ZCodeParser.ParamcallContext):
        pass

    # Exit a parse tree produced by ZCodeParser#paramcall.
    def exitParamcall(self, ctx:ZCodeParser.ParamcallContext):
        pass


    # Enter a parse tree produced by ZCodeParser#blockstmt.
    def enterBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#blockstmt.
    def exitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_list.
    def enterStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_list.
    def exitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt_prime.
    def enterStmt_prime(self, ctx:ZCodeParser.Stmt_primeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt_prime.
    def exitStmt_prime(self, ctx:ZCodeParser.Stmt_primeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#stmt.
    def enterStmt(self, ctx:ZCodeParser.StmtContext):
        pass

    # Exit a parse tree produced by ZCodeParser#stmt.
    def exitStmt(self, ctx:ZCodeParser.StmtContext):
        pass


    # Enter a parse tree produced by ZCodeParser#nullable_newline_list.
    def enterNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#nullable_newline_list.
    def exitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#newline_list.
    def enterNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#newline_list.
    def exitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        pass



del ZCodeParser