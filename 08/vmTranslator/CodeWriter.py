
from Parser import CmdType


class CodeWriter:

    def __init__(self, output_file):
        self.file = open(output_file, 'w')
        self.function = ''
        self.functionCalls = {}
        self.cmd_no = -1
        self.staticFile = ''
        self.segments = {
            'local': 'LCL',
            'argument': 'ARG',
            'this': 'THIS',
            'that': 'THAT',
        }
        self.arithOpsDualOps = {
            'add': 'M+D',
            'sub': 'M-D',
            'and': 'D&M',
            'or': 'D|M',
        }

        self.arithOpsSingleOps = {
            'neg': '-M',
            'not': '!M'
        }

        self.arithComparisonOps = {
            'eq': 'D;JEQ',
            'gt': 'D;JGT',
            'lt': 'D;JLT',
        }

        self.pointers = {
            '0': 'THIS',
            '1': 'THAT',
        }

    def incCmd(self):
        self.cmd_no += 1
        return self.cmd_no

    def setFileName(self, staticFile):
        self.staticFile = staticFile

    def writeArithmetic(self, command):
        hack_cmds = [f'\n// {command}']
        hack_cmds += [f'{x} // {self.incCmd()}' for x in ['@SP',
                                                          'M=M-1',
                                                          '@SP',
                                                          'A=M']]
        if command in self.arithOpsSingleOps:
            hack_cmds += [f'{x} // {self.incCmd()}' for x in [f'M={self.arithOpsSingleOps[command]}',
                                                              '@SP',
                                                              'M=M+1'
                                                              ]]

        elif command in self.arithOpsDualOps:
            hack_cmds += [f'{x} // {self.incCmd()}' for x in ['D=M',
                                                              '@SP',
                                                              'M=M-1',
                                                              '@SP',
                                                              'A=M',
                                                              f'M={self.arithOpsDualOps[command]}',
                                                              '@SP',
                                                              'M=M+1']]
        elif command in self.arithComparisonOps:
            hack_cmds += [f'{x} // {self.incCmd()}' for x in ['D=M',
                                                              '@SP',
                                                              'M=M-1',
                                                              '@SP',
                                                              'A=M',
                                                              'D=M-D',
                                                              'M=-1',
                                                              f'@FALSE_JUMP_{self.cmd_no}',
                                                              f'{self.arithComparisonOps[command]}',
                                                              '@SP',
                                                              'A=M',
                                                              'M=0',
                                                              f'(FALSE_JUMP_{self.cmd_no})',
                                                              '@SP',
                                                              'M=M+1'
                                                              ]]

        self.file.write('\n\t'.join(hack_cmds))

    def writePushPop(self, cmdType, segment, index):
        hack_cmds = [f'\n// {cmdType.value} {segment} {index}']
        if segment in self.segments:
            hack_cmds += [f'{x} // {self.incCmd()}' for x in [f'@{index}',
                                                              'D=A',
                                                              f"@{self.segments[segment]}"]]

            if cmdType == CmdType.C_PUSH:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in ['A=M+D',
                                                                  'D=M',
                                                                  '@SP',
                                                                  'A=M',
                                                                  'M=D',
                                                                  '@SP',
                                                                  'M=M+1']]
            elif cmdType == CmdType.C_POP:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in ['D=M+D',
                                                                  '@R13',
                                                                  'M=D',
                                                                  '@SP',
                                                                  'M=M-1',
                                                                  'A=M',
                                                                  'D=M',
                                                                  '@R13',
                                                                  'A=M',
                                                                  'M=D']]
        elif segment == 'constant':
            hack_cmds += [f'{x} // {self.incCmd()}' for x in [f'@{index}',
                                                              'D=A',
                                                              '@SP',
                                                              'A=M',
                                                              'M=D',
                                                              '@SP',
                                                              'M=M+1']]
        elif segment == 'temp':
            if cmdType == CmdType.C_PUSH:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in [f"@R{5 + int(index)}",
                                                                  'D=M',
                                                                  '@SP',
                                                                  'A=M',
                                                                  'M=D',
                                                                  '@SP',
                                                                  'M=M+1']]
            elif cmdType == CmdType.C_POP:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in ['@SP',
                                                                  'M=M-1',
                                                                  'A=M',
                                                                  'D=M',
                                                                  f"@R{5 + int(index)}",
                                                                  'M=D']]
        elif segment == 'pointer' or segment == 'static':
            location = f'{self.staticFile}.{index}' if segment == 'static' else f'{self.pointers[index]}'
            if cmdType == CmdType.C_PUSH:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in [f"@{location}",
                                                                  "D=M",
                                                                  "@SP",
                                                                  "A=M",
                                                                  "M=D",
                                                                  "@SP",
                                                                  "M=M+1"]]
            elif cmdType == CmdType.C_POP:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in ["@SP",
                                                                  'M=M-1',
                                                                  'A=M',
                                                                  'D=M',
                                                                  f"@{location}",
                                                                  'M=D']]
        elif segment == 'location':
            if cmdType == CmdType.C_PUSH:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in [f"@{index}",
                                                                  "D=M",
                                                                  "@SP",
                                                                  "A=M",
                                                                  "M=D",
                                                                  "@SP",
                                                                  "M=M+1"]]
            elif cmdType == CmdType.C_POP:
                hack_cmds += [f'{x} // {self.incCmd()}' for x in ["@SP",
                                                                  'M=M-1',
                                                                  'A=M',
                                                                  'D=M',
                                                                  f"@{index}",
                                                                  'M=D']]

        self.file.write('\n\t'.join(hack_cmds))

    def writeInit(self):
        self.function = "Sys.init"
        self.file.write(f'\n// init\n\t')
        hack_cmds = [f'{x} // {self.incCmd()}' for x in ["@256",
                                                         "D=A",
                                                         "@SP",
                                                         "M=D",
                                                         ]]
        self.file.write('\n\t'.join(hack_cmds))
        self.writeCall(self.function, 0)

    def writeLabel(self, label, includeFunc=False):
        if includeFunc:
            self.file.write(f'\n({self.function}${label})')
        else:
            self.file.write(f'\n({label})')

    def writeGoto(self, label, includeFunc=False):
        if includeFunc:
            label = f'{self.function}${label}'
        hack_cmds = [f'\n// goto {label}']
        hack_cmds += [f'{x} // {self.incCmd()}' for x in [f"@{label}", "0;JMP"]]
        self.file.write('\n\t'.join(hack_cmds))

    def writeIf(self, label, includeFunc=False):
        if includeFunc:
            label = f'{self.function}${label}'
        hack_cmds = [f'\n// goto-if {label}']
        hack_cmds += [f'{x} // {self.incCmd()}' for x in ["@SP",
                                                          'M=M-1',
                                                          'A=M',
                                                          'D=M',
                                                          f"@{label}",
                                                          "D;JNE"]]
        self.file.write('\n\t'.join(hack_cmds))

    def writeFunction(self, function, nVars):
        self.function = function
        self.file.write(f'\n// function {function} {nVars}')
        self.writeLabel(function)
        hack_cmds = ['']
        for i in range(int(nVars)):
            hack_cmds += [f'{x} // {self.incCmd()}' for x in ["@SP",
                                                              "A=M",
                                                              "M=0",
                                                              "@SP",
                                                              "M=M+1"]]
        self.file.write('\n\t'.join(hack_cmds))

    def writeCall(self, function, nVars):
        if function not in self.functionCalls:
            self.functionCalls[function] = 1
        else:
            self.functionCalls[function] += 1
        self.file.write(f'\n// call {function} {nVars}\n\t')
        hack_cmds = [f'{x} // {self.incCmd()}' for x in [f'@{function}$ret.{self.functionCalls[function]}',
                                                         "D=A",
                                                         "@SP",
                                                         "A=M",
                                                         "M=D",
                                                         "@SP",
                                                         "M=M+1"]]
        self.file.write('\n\t'.join(hack_cmds))
        self.writePushPop(CmdType.C_PUSH, 'location', 'LCL')
        self.writePushPop(CmdType.C_PUSH, 'location', 'ARG')
        self.writePushPop(CmdType.C_PUSH, 'pointer', '0')
        self.writePushPop(CmdType.C_PUSH, 'pointer', '1')
        hack_cmds = [f'{x} // {self.incCmd()}' for x in ["\n\t@SP",
                                                         'D=M',
                                                         "@5",
                                                         'D=D-A',
                                                         f'@{nVars}',
                                                         'D=D-A',
                                                         '@ARG',
                                                         'M=D',
                                                         '@SP',
                                                         'D=M',
                                                         '@LCL',
                                                         'M=D'
                                                         ]]
        self.file.write('\n\t'.join(hack_cmds))
        self.writeGoto(function)
        self.writeLabel(f'{function}$ret.{self.functionCalls[function]}')

    def writeReturn(self):
        self.file.write('\n// return')
        hack_cmds = [f'{x} // {self.incCmd()}' for x in ["\n\t@LCL",
                                                         'D=M',

                                                         '@R13',
                                                         'M=D',
                                                         '@5',
                                                         'D=D-A',
                                                         'A=D',
                                                         'D=M',
                                                         '@R14',
                                                         'M=D',

                                                         '@SP',
                                                         'M=M-1',
                                                         'A=M',
                                                         'D=M',
                                                         '@ARG',
                                                         'A=M',
                                                         'M=D',

                                                         '@ARG',
                                                         'D=M+1',
                                                         '@SP',
                                                         'M=D',

                                                         '@R13',
                                                         'A=M-1',
                                                         'D=M',
                                                         '@THAT',
                                                         'M=D',

                                                         '@R2',
                                                         'D=A',
                                                         '@R13',
                                                         'A=M-D',
                                                         'D=M',
                                                         '@THIS',
                                                         'M=D',

                                                         '@R3',
                                                         'D=A',
                                                         '@R13',
                                                         'A=M-D',
                                                         'D=M',
                                                         '@ARG',
                                                         'M=D',

                                                         '@R4',
                                                         'D=A',
                                                         '@R13',
                                                         'A=M-D',
                                                         'D=M',
                                                         '@LCL',
                                                         'M=D',

                                                         '@R14',
                                                         'A=M',
                                                         '0;JMP'
                                                         ]]
        self.file.write('\n\t'.join(hack_cmds))

    def __del__(self):
        self.file.close()
