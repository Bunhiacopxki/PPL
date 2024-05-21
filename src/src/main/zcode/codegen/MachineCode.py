'''
*   @author Dr.Nguyen Hua Phung
*   @version 1.0
*   28/6/2006
*   This class provides facilities for method generation
*
'''
from abc import ABC, abstractmethod, ABCMeta

class MachineCode(ABC):
    @abstractmethod
    def emitICONST(self, i):
        pass
    @abstractmethod
    def emitIADD(self):
        pass
    @abstractmethod
    def emitINVOKEFUNCTION(self, lexeme):
        pass
    @abstractmethod
    def emitMETHOD(self, lexeme):
        pass


class MipsCode(MachineCode):
    END = "\n"
    INDENT = "\t"

    def emitCONST(self, register, name):
        return MipsCode.INDENT + "l.s $" + register + ", " + name + MipsCode.END

    def emitICONST(self, i, value):
        # return MipsCode.INDENT + "l.s $" + register + ", " + str(i) + MipsCode.END
        return MipsCode.END + MipsCode.INDENT \
                + ".data\n" + i + ": .float " + str(value) + MipsCode.END
    
    def emitBUFFER(self, var):
        return MipsCode.END + MipsCode.INDENT + ".data\n" + var + ": .space 100"+ MipsCode.END
    
    def emitSTRING(self, string, var):
        return MipsCode.END + MipsCode.INDENT \
            + ".data\n" + var + ": .asciiz " + "\"" + string + "\"" + MipsCode.END

    def emitIADD(self, register1, register2, des_register) -> str:
        return MipsCode.INDENT + "add.s $" + des_register + ", $" + register1 + ", $" + register2 + MipsCode.END
    
    def emitISUB(self, register1, register2, des_register) -> str:
        return MipsCode.INDENT + "sub.s $" + des_register + ", $" + register1 + ", $" + register2 + MipsCode.END
    
    def emitIMUL(self, register1, register2, des_register) -> str:
        return MipsCode.INDENT + "mul.s $" + des_register + ", $" + register1 + ", $" + register2 + MipsCode.END
    
    def emitINEG(self, register1, des_register) -> str:
        return MipsCode.INDENT + "neg.s $" + des_register + ", $" + register1 + MipsCode.END
    
    # def emitRELOP(self, register1, register2, des_register) -> str:
    #     return MipsCode.INDENT + "c.lt.s $" + des_register + ", $" + register1 + ", $" + register2 + MipsCode.END
    
    def emitINVOKEFUNCTION(self, lexeme):
        return MipsCode.INDENT + "jal " + lexeme + MipsCode.END
    
    def emitLOADSYSCALL(self, reg_des):
        return MipsCode.INDENT + "mov.s $f12, $" + reg_des + MipsCode.END
    
    def emitLOADSYSCALL_PRINTSTRING(self, var):
        return MipsCode.INDENT + "la $a0, " + var + MipsCode.END
    
    def emitLOADSYSCALL_PRINTBOOL(self, var):
        return MipsCode.INDENT + "la $a0, " + var + MipsCode.END
    
    def emitATTRIBUTE(self, register, name, indent):
        if indent == True:
            return MipsCode.INDENT + "l.s $" + register + ", " + name + MipsCode.END
        return "l.s $" + register + ", " + name + MipsCode.END
    
    def emitATTRIBUTE_MOVE(self, register, register2, indent):
        if indent == True:
            return MipsCode.INDENT + "mov.s $" + register + ", " + register2 + MipsCode.END
        return "mov.s $" + register + ", " + register2 + MipsCode.END
    
    def emitGETATTRIBUTE(self, register):
        return MipsCode.INDENT + "mov.s $t1, " + register + MipsCode.END
    
    def emitGETSTRINGATTRIBUTE(self, register, name):
        return MipsCode.INDENT + "la $" + register + ", " + name + MipsCode.END

    def emitMETHOD(self, lexeme):
        return MipsCode.END + lexeme + ":" + MipsCode.END
        
    
