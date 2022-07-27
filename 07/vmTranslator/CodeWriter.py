
from Parser import CmdType


class CodeWriter:

    def __init__(self, output_file):
        self.staticFile = output_file.rsplit('/', 1)[1].replace('.asm', '')
        self.file = open(output_file, 'w')
        self.cmd_no = -1
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

        self.file.write('\n'.join(hack_cmds))

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

        self.file.write('\n'.join(hack_cmds))

    def __del__(self):
        self.file.close()
