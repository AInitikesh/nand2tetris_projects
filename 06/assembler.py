import sys

input_file = sys.argv[1]

lines = []
with open(input_file) as f:
    lines = f.readlines()


class Assembler:

    def __init__(self, lines):
        self.compute_instruct = {
            '': '000000',
            '0': '101010',
            '1': '111111',
            '-1': '111010',
            'D': '001100',
            'A': '110000',
            '!D': '001101',
            '!A': '110001',
            '-D': '001111',
            '-A': '110011',
            'D+1': '011111',
            'A+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'D+A': '000010',
            'D-A': '010011',
            'A-D': '000111',
            'D&A': '000000',
            'D|A': '010101',
            'M': '110000',
            '!M': '110001',
            '-M': '110011',
            'M+1': '110111',
            'M-1': '110010',
            'D+M': '000010',
            'D-M': '010011',
            'M-D': '000111',
            'D&M': '000000',
            'D|M': '010101'
        }

        self.dest_instruct = {
            '': '000',
            'M': '001',
            'D': '010',
            'MD': '011',
            'A': '100',
            'AM': '101',
            'AD': '110',
            'AMD': '111'
        }

        self.jump_instruct = {
            '': '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }

        self.symbol_table = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }

        self.instruction_lines = []
        self.preprocess(lines)
        self.register = 16

    def preprocess(self, lines):
        line_no = 0
        for i in range(len(lines)):
            line = lines[i]
            line = line.strip()
            line = line.split('//')[0]
            if line != '':
                if line.startswith('(') and line.endswith(')'):
                    self.symbol_table[line[1:-1]] = line_no
                else:
                    line_no += 1
                    self.instruction_lines.append(line)

    def command_type(self, cmd):
        if cmd[0] == '@':
            return 0
        else:
            return 1

    def a_command(self, cmd):
        cmd = cmd.strip('@')
        if not cmd.isdigit():
            if cmd not in self.symbol_table:
                self.symbol_table[cmd] = self.register
                self.register += 1
            cmd = str(self.symbol_table[cmd])
        return '0' + bin(int(cmd))[2:].zfill(15)

    def c_command(self, cmd):
        cmd = cmd.split(';')
        op, jmp = cmd[0], cmd[1].strip() if len(cmd) > 1 else ''
        op = list(reversed(op.split('=')))
        comp, dest = op[0].strip(), op[1].strip() if len(op) > 1 else ''
        a = '1' if 'M' in comp else '0'
        print
        return '111' + a + self.compute_instruct[comp] + self.dest_instruct[dest] + self.jump_instruct[jmp]

    def process_lines(self):
        hack_commands = []
        for x in self.instruction_lines:
            if x.startswith('(') and x.endswith(')'):
                continue
            if asm.command_type(x) == 0:
                hack_commands.append(asm.a_command(x))
            else:
                hack_commands.append(asm.c_command(x))
        return hack_commands


asm = Assembler(lines)
hack_commands = asm.process_lines()

with open(input_file.split('.')[0] + '.hack', 'w') as f:
    for x in hack_commands:
        f.write(x + '\n')
