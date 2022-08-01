from enum import Enum
from JackTokenizer import KeyWord

class KeyWordArg(Enum):
    ARG = 'argument'

class SymbolTable:
    
    def __init__(self):
        self.class_dict = {}
        self.subroutine_dict = {}
        self.type_count = {KeyWord.STATIC: 0, KeyWord.FIELD: 0, KeyWordArg.ARG: 0, KeyWord.VAR: 0}
    
    def startSubroutine(self):
        self.subroutine_dict = {}
        self.type_count[KeyWordArg.ARG] = 0
        self.type_count[KeyWord.VAR] = 0
    
    def define(self, name, fieldType, kind):
        if kind in (KeyWord.STATIC, KeyWord.FIELD):
            self.class_dict[name] = (fieldType, kind, self.varCount(kind))
            self.type_count[kind] +=1
        elif kind in (KeyWordArg.ARG, KeyWord.VAR):
            self.subroutine_dict[name] = (fieldType, kind, self.varCount(kind))
            self.type_count[kind] +=1
        else:
            raise Exception('Invalid kind: ' + kind)
        
    
    def varCount(self, kind):
        return self.type_count[kind]
    
    def kindOf(self, name):
        if name in self.subroutine_dict:
            return self.subroutine_dict[name][1]
        elif name in self.class_dict:
            return self.class_dict[name][1]
        else:
            return None
    
    def typeOf(self, name):
        if name in self.subroutine_dict:
            return self.subroutine_dict[name][0]
        elif name in self.class_dict:
            return self.class_dict[name][0]
        else:
            return None
    
    def indexOf(self, name):
        if name in self.subroutine_dict:
            return self.subroutine_dict[name][2]
        elif name in self.class_dict:
            return self.class_dict[name][2]
        else:
            return None
    
    