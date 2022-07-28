import os
import sys
from glob import glob
from CompilationEngine import CompilationEngine
from JackTokenizer import JackTokenizer, TokenType, KeyWord

input = sys.argv[1]

if os.path.isdir(input):
    input_files = glob(input + '/*.jack')
else:
    input_files = [input]

for input_file in input_files:
    print("Processing file ", input_file)
    output_token_file = input_file.replace('.jack', '_T.xml')
    tokenizer = JackTokenizer(input_file)
    with open(output_token_file, 'w') as f:
        f.write('<tokens>\n')
        while tokenizer.hasMoreTokens():
            tokenizer.advance()
            tokenType = tokenizer.tokenType()
            match tokenType:
                case TokenType.KEYWORD:
                    keyword = tokenizer.keyWord()
                    match keyword:
                        case KeyWord.CLASS:
                            f.write('<keyword> class </keyword>\n')
                        case KeyWord.CONSTRUCTOR:
                            f.write('<keyword> constructor </keyword>\n')
                        case KeyWord.FUNCTION:
                            f.write('<keyword> function </keyword>\n')
                        case KeyWord.METHOD:
                            f.write('<keyword> method </keyword>\n')
                        case KeyWord.INT:
                            f.write('<keyword> int </keyword>\n')
                        case KeyWord.BOOLEAN:
                            f.write('<keyword> boolean </keyword>\n')
                        case KeyWord.CHAR:
                            f.write('<keyword> char </keyword>\n')
                        case KeyWord.VOID:
                            f.write('<keyword> void </keyword>\n')
                        case KeyWord.FIELD:
                            f.write('<keyword> field </keyword>\n')
                        case KeyWord.STATIC:
                            f.write('<keyword> static </keyword>\n')
                        case KeyWord.LET:
                            f.write('<keyword> let </keyword>\n')
                        case KeyWord.DO:
                            f.write('<keyword> do </keyword>\n')
                        case KeyWord.IF:
                            f.write('<keyword> if </keyword>\n')
                        case KeyWord.ELSE:
                            f.write('<keyword> else </keyword>\n')
                        case KeyWord.WHILE:
                            f.write('<keyword> while </keyword>\n')
                        case KeyWord.RETURN:
                            f.write('<keyword> return </keyword>\n')
                        case KeyWord.TRUE:
                            f.write('<keyword> true </keyword>\n')
                        case KeyWord.FALSE:
                            f.write('<keyword> false </keyword>\n')
                        case KeyWord.NULL:
                            f.write('<keyword> null </keyword>\n')
                        case KeyWord.THIS:
                            f.write('<keyword> this </keyword>\n')
                        case KeyWord.VAR:
                            f.write('<keyword> var </keyword>\n')
                case TokenType.SYMBOL:
                    symbol = tokenizer.symbol()
                    f.write('<symbol> ' + symbol + ' </symbol>\n')
                case TokenType.IDENTIFIER:
                    identifier = tokenizer.identifier()
                    f.write('<identifier> ' + identifier + ' </identifier>\n')
                case TokenType.INT_CONST:
                    intVal = tokenizer.intVal()
                    f.write('<integerConstant> ' +
                            intVal + ' </integerConstant>\n')
                case TokenType.STRING_CONST:
                    stringVal = tokenizer.stringVal()
                    f.write('<stringConstant> ' +
                            stringVal + ' </stringConstant>\n')
        f.write('</tokens>\n')
        output_file = input_file.replace('.jack', '_.xml')
        CompilationEngine(input_file, output_file)
