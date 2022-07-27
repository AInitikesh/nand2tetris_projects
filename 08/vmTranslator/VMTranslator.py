import os
import sys
from glob import glob
from Parser import Parser, CmdType
from CodeWriter import CodeWriter

input = sys.argv[1]


if os.path.isfile(input):
    input_files = [input]
    output_file = input.replace('.vm', '.asm')
else:
    input_files = glob(input + '/*.vm')
    if input.endswith('/'):
        input = input[:-1]
    output_file = os.path.join(input, input.rsplit('/', 1)[-1] + '.asm')
codeWriter = CodeWriter(output_file)
print(output_file)
for input_file in input_files:
    with open(input_file) as f:
        content = "\n".join([x.split('//')[0] for x in f.read().split('\n')])
        if "Sys.init" in content:
            codeWriter.writeInit()

for input_file in input_files:
    parser = Parser(input_file)
    while parser.hasMoreCommands():
        parser.advance()
        cmdType = parser.commandType()
        codeWriter.setFileName(input_file.rsplit('/', 1)[1].replace('.vm', ''))
        if cmdType == CmdType.C_PUSH or cmdType == CmdType.C_POP:
            codeWriter.writePushPop(cmdType, *parser.arg2())
        elif cmdType == CmdType.C_ARITHMETIC:
            codeWriter.writeArithmetic(parser.arg1())
        elif cmdType == CmdType.C_LABEL:
            codeWriter.writeLabel(*parser.arg2(), includeFunc=True)
        elif cmdType == CmdType.C_GOTO:
            codeWriter.writeGoto(*parser.arg2(), includeFunc=True)
        elif cmdType == CmdType.C_IF:
            codeWriter.writeIf(*parser.arg2(), includeFunc=True)
        elif cmdType == CmdType.C_FUNCTION:
            codeWriter.writeFunction(*parser.arg2())
        elif cmdType == CmdType.C_CALL:
            codeWriter.writeCall(*parser.arg2())
        elif cmdType == CmdType.C_RETURN:
            codeWriter.writeReturn(*parser.arg2())
