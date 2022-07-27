import sys
from Parser import Parser, CmdType
from CodeWriter import CodeWriter

input_file = sys.argv[1]
output_file = input_file.replace('.vm', '.asm')

parser = Parser(input_file)
codeWriter = CodeWriter(output_file)

while parser.hasMoreCommands():
    parser.advance()
    cmdType = parser.commandType()
    if cmdType == CmdType.C_PUSH or cmdType == CmdType.C_POP:
        print(cmdType, *parser.arg2())
        codeWriter.writePushPop(cmdType, *parser.arg2())
    elif cmdType == CmdType.C_ARITHMETIC:
        codeWriter.writeArithmetic(parser.arg1())
        print(parser.arg1())
