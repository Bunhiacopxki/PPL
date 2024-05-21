import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """
        number a <- 2
        func main()
        begin
            number b <- 3
            putInt(a * b + 1 + 2 + 3*4)
        end
        """
        expect = "Program([FuncDecl(Id(main), [], Block([VarDecl(Id(a), NumberType, None, NumLit(2.0)), CallStmt(Id(putInt), [BinaryOp(+, Id(a), NumLit(1.0))])]))])"
        self.assertTrue(TestAST.test(input,expect,300))
   