import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # def test_501(self):
    #     input = """func main()
    #     begin
    #         writeNumber(1+1)
    #     end
    #     """
    #     expect = "2.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,501))
        
    # def test_502(self):
    #     input = """
    #     func foo()
    #     begin
    #         writeNumber(1+1)
    #     end
    #     func main()
    #     begin
    #         foo()
    #     end
    #     """
    #     expect = "2.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,502))

    # def test_503(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- readNumber()
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,503))

    # def test_504(self):
    #     input = """
    #     func main()
    #     begin
    #         string a <- "abc"
    #         writeString("cde")
    #         writeString("abc" ... a)
    #     end
    #     """
    #     expect = "cdeabcabc\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,504))

    # def test_505(self):
    #     input = """
    #     func main()
    #     begin
    #         string a <- "abc"
    #         string b <- "cde"
    #         string c <- a ... b
    #         string d <- "1"
    #         string e <- "2"
    #         string f <- d ... e
    #         writeString(c)
    #         writeString(f)
    #     end
    #     """
    #     expect = "abccde12\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_506(self):
        input = """
        func main()
        begin
            writeBool(true)
        end
        """
        expect = "true\n"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    # def test_507(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- 2
    #         writeNumber(-(a+1))
    #     end
    #     """
    #     expect = "-3.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,507))

    # def test_508(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- 2
    #         writeNumber(a)
    #     end
    #     """
    #     expect = "2.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,508))

    # def test_509(self):
    #     input = """
    #     func main()
    #     begin
    #         number a <- 2
    #         writeNumber(a * 3 - 5 + 10)
    #     end
    #     """
    #     expect = "11.0\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,509))

    # def test_510(self):
    #     input = """
    #     func main()
    #     begin
    #         bool a <- true
    #         writeBool(a)
    #     end
    #     """
    #     expect = "true\n"
    #     self.assertTrue(TestCodeGen.test(input,expect,510))



