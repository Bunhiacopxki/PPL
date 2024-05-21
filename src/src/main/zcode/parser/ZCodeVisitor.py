# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl_list.
    def visitDecl_list(self, ctx:ZCodeParser.Decl_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#decl.
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl.
    def visitVar_decl(self, ctx:ZCodeParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_decl_part.
    def visitVar_decl_part(self, ctx:ZCodeParser.Var_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_vardecl.
    def visitOptional_vardecl(self, ctx:ZCodeParser.Optional_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#must_vardecl.
    def visitMust_vardecl(self, ctx:ZCodeParser.Must_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_decl.
    def visitArr_decl(self, ctx:ZCodeParser.Arr_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_size_list.
    def visitArr_size_list(self, ctx:ZCodeParser.Arr_size_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#arr_size_prime.
    def visitArr_size_prime(self, ctx:ZCodeParser.Arr_size_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#scalar_type.
    def visitScalar_type(self, ctx:ZCodeParser.Scalar_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_initialize.
    def visitOptional_initialize(self, ctx:ZCodeParser.Optional_initializeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#initialize.
    def visitInitialize(self, ctx:ZCodeParser.InitializeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_decl.
    def visitFunc_decl(self, ctx:ZCodeParser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_decl.
    def visitParam_decl(self, ctx:ZCodeParser.Param_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_prime.
    def visitParam_prime(self, ctx:ZCodeParser.Param_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_name.
    def visitParam_name(self, ctx:ZCodeParser.Param_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#endfunc.
    def visitEndfunc(self, ctx:ZCodeParser.EndfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assignstmt.
    def visitAssignstmt(self, ctx:ZCodeParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lhs.
    def visitLhs(self, ctx:ZCodeParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr.
    def visitExpr(self, ctx:ZCodeParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr1.
    def visitExpr1(self, ctx:ZCodeParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr2.
    def visitExpr2(self, ctx:ZCodeParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr3.
    def visitExpr3(self, ctx:ZCodeParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr4.
    def visitExpr4(self, ctx:ZCodeParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr5.
    def visitExpr5(self, ctx:ZCodeParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr6.
    def visitExpr6(self, ctx:ZCodeParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr7.
    def visitExpr7(self, ctx:ZCodeParser.Expr7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr8.
    def visitExpr8(self, ctx:ZCodeParser.Expr8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr9.
    def visitExpr9(self, ctx:ZCodeParser.Expr9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operation.
    def visitIndex_operation(self, ctx:ZCodeParser.Index_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_operators.
    def visitIndex_operators(self, ctx:ZCodeParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#ifstmt.
    def visitIfstmt(self, ctx:ZCodeParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#cond_block.
    def visitCond_block(self, ctx:ZCodeParser.Cond_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_elif_list.
    def visitOptional_elif_list(self, ctx:ZCodeParser.Optional_elif_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_elif.
    def visitOptional_elif(self, ctx:ZCodeParser.Optional_elifContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_else.
    def visitOptional_else(self, ctx:ZCodeParser.Optional_elseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forstmt.
    def visitForstmt(self, ctx:ZCodeParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#breakstmt.
    def visitBreakstmt(self, ctx:ZCodeParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continuestmt.
    def visitContinuestmt(self, ctx:ZCodeParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#returnstmt.
    def visitReturnstmt(self, ctx:ZCodeParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#callstmt.
    def visitCallstmt(self, ctx:ZCodeParser.CallstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramcall_part.
    def visitParamcall_part(self, ctx:ZCodeParser.Paramcall_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramcall_list.
    def visitParamcall_list(self, ctx:ZCodeParser.Paramcall_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramcall_prime.
    def visitParamcall_prime(self, ctx:ZCodeParser.Paramcall_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#paramcall.
    def visitParamcall(self, ctx:ZCodeParser.ParamcallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#blockstmt.
    def visitBlockstmt(self, ctx:ZCodeParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_list.
    def visitStmt_list(self, ctx:ZCodeParser.Stmt_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt_prime.
    def visitStmt_prime(self, ctx:ZCodeParser.Stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#stmt.
    def visitStmt(self, ctx:ZCodeParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#nullable_newline_list.
    def visitNullable_newline_list(self, ctx:ZCodeParser.Nullable_newline_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#newline_list.
    def visitNewline_list(self, ctx:ZCodeParser.Newline_listContext):
        return self.visitChildren(ctx)



del ZCodeParser