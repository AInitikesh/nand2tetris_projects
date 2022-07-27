from enum import Enum
    

class CmdType(Enum):
    C_ARITHMETIC = 'C_ARITHMETIC'
    C_PUSH = 'C_PUSH'
    C_POP = 'C_POP'
    C_LABEL = 'C_LABEL'
    C_GOTO = 'C_GOTO'
    C_IF = 'C_IF'
    C_FUNCTION = 'C_FUNCTION'
    C_RETURN = 'C_RETURN'
    C_CALL = 'C_CALL'

class Parser:

    def __init__(self, input_file):
        self.current_index = -1
        lines = self.readFile(input_file)
        self.preprocess(lines)

    def readFile(self, input_file):

        with (open(input_file, 'r')) as f:
            lines = f.readlines()
        return lines

    def preprocess(self, lines):
        self.cmds = []
        for i in range(len(lines)):
            line = lines[i]
            line = line.split('//')[0]
            line = line.strip()
            if line != '':
                splits = line.split(' ')
                splits = [x.strip() for x in splits]
                self.cmds.append(splits)

    def hasMoreCommands(self):
        return self.current_index + 1 < len(self.cmds)
    
    def advance(self):          
        self.current_index += 1
        self.current_command = self.cmds[self.current_index]
            
        
    def commandType(self):
        if self.current_command[0] == 'push':
                return CmdType.C_PUSH
        elif self.current_command[0] == 'pop':
                return CmdType.C_POP
        elif self.current_command[0] in ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not'):
                return CmdType.C_ARITHMETIC
        else:
            return None
        
    def arg1(self):
            return self.current_command[0]
    
    def arg2(self):
        return self.current_command[1:]
    