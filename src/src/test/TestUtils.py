import sys,os
from antlr4 import *
from antlr4.error.ErrorListener import ConsoleErrorListener,ErrorListener
if not './main/zcode/parser/' in sys.path:
    sys.path.append('./main/zcode/parser/')
if os.path.isdir('../target/main/zcode/parser') and not '../target/main/zcode/parser/' in sys.path:
    sys.path.append('../target/main/zcode/parser/')
from ZCodeLexer import ZCodeLexer
from ZCodeParser import ZCodeParser
from lexererr import *
from ASTGeneration import ASTGeneration
from StaticCheck import StaticChecker
from StaticError import *
from CodeGenerator import CodeGenerator
import subprocess

# JASMIN_JAR = "./external/jasmin.jar"
MARS_JAR = "./external/Mars4_5.jar"
IO_ASM = './lib/io.asm'
TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"
Lexer = ZCodeLexer
Parser = ZCodeParser

class TestUtil:
    @staticmethod
    def makeSource(inputStr,num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename,"w")
        file.write(inputStr)
        file.close()
        return FileStream(filename)


class TestLexer:
    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestLexer.check(SOL_DIR,inputfile,num)
        dest = open(SOL_DIR + str(num) + ".txt","r")
        line = dest.read()
        return line == expect
    
    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(os.path.join(soldir,str(num) + ".txt"),"w")
        lexer = Lexer(inputfile)
        try:
            TestLexer.printLexeme(dest,lexer)
        except (ErrorToken,UncloseString,IllegalEscape) as err:
            dest.write(err.message)
        finally:
            dest.close() 

    @staticmethod    
    def printLexeme(dest,lexer):
        tok = lexer.nextToken()
        if tok.type != Token.EOF:
            dest.write(tok.text+",")
            TestLexer.printLexeme(dest,lexer)
        else:
            dest.write("<EOF>")

class NewErrorListener(ConsoleErrorListener):
    INSTANCE = None
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Error on line "+ str(line) + " col " + str(column)+ ": " + offendingSymbol.text)
NewErrorListener.INSTANCE = NewErrorListener()

class SyntaxException(Exception):
    def __init__(self,msg):
        self.message = msg

class TestParser:
    @staticmethod
    def createErrorListener():
         return NewErrorListener.INSTANCE

    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestParser.check(SOL_DIR,inputfile,num)
        dest = open(SOL_DIR + str(num) + ".txt","r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(os.path.join(soldir , str(num) + ".txt"),"w")
        lexer = Lexer(inputfile)
        listener = TestParser.createErrorListener()
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        try:
            parser.program()
            dest.write("successful")
        except SyntaxException as f:
            dest.write(f.message)
        except Exception as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestAST:
    @staticmethod
    def test(input,expect,num):
        inputfile = TestUtil.makeSource(input,num)
        TestAST.check(SOL_DIR,inputfile,num)
        dest = open(os.path.join(SOL_DIR,str(num) + ".txt"),"r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,inputfile,num):
        dest = open(os.path.join(soldir,str(num) + ".txt"),"w")
        lexer = Lexer(inputfile)
        tokens = CommonTokenStream(lexer)
        parser = Parser(tokens)
        tree = parser.program()
        asttree = ASTGeneration().visit(tree)
        dest.write(str(asttree))
        dest.close()

class TestChecker:
    @staticmethod
    def test(input,expect,num):       
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input       
        TestChecker.check(SOL_DIR,asttree,num)
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"),"r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,asttree,num):  
        dest = open(os.path.join(soldir, str(num) + ".txt"),"w")     
        checker = StaticChecker(asttree)
        try:
            res = checker.check()
            dest.write(str(list(res)))
        except StaticError as e:
            dest.write(str(e))
        finally:
            dest.close()

class TestCodeGen():
    @staticmethod
    def test(input, expect, num):
        if type(input) is str:
            inputfile = TestUtil.makeSource(input,num)
            lexer = Lexer(inputfile)
            tokens = CommonTokenStream(lexer)
            parser = Parser(tokens)
            tree = parser.program()
            asttree = ASTGeneration().visit(tree)
        else:
            inputfile = TestUtil.makeSource(str(input),num)
            asttree = input
        
        TestCodeGen.check(SOL_DIR,asttree,num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"),"r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir,asttree,num):
        codeGen = CodeGenerator()
        path = os.path.join(soldir, str(num))
        if not os.path.isdir(path):
            os.mkdir(path)
        f = open(os.path.join(soldir, str(num) + ".txt"),"w")
        try:
            codeGen.gen(asttree, path)
            
            # subprocess.call("java  -jar "+ JASMIN_JAR + " " + path + "/ZCodeClass.j",shell=True,stderr=subprocess.STDOUT)
            # cmd = "java  -jar "+ MARS_JAR + " " + path + "/ZCodeClass.asm" + " " + IO_ASM + " nc"
            cmd = "java  -jar "+ MARS_JAR + " " + path + "/ZCodeClass.asm" + " nc"
            # subprocess.call(temp, shell=True,stderr=subprocess.STDOUT)
            # cmd = "java -cp ./lib" + os.pathsep +". ZCodeClass"
            subprocess.run(cmd, shell=True, stdout = f, timeout=10)
        except StaticError as e:
            f.write(str(e))
        except subprocess.TimeoutExpired:
            f.write("Time out\n")
        except subprocess.CalledProcessError as e:
            raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))
        finally:
            f.close()
            
            
