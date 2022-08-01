from SymbolTable import KeyWordArg
from JackTokenizer import JackTokenizer, TokenType, KeyWord
from VMWriter import VMWriter
from SymbolTable import SymbolTable


class CompilationEngine:

    def __init__(self, input_file, output_file):
        self.tokenizer = JackTokenizer(input_file)
        self.vmWriter = VMWriter(output_file)
        self.symbolTable = SymbolTable()
        self.op = {'+': 'add', '-': 'sub', '*': 'call Math.multiply 2', '/': 'call Math.divide 2',
                   '&amp;': 'and', '|': 'or', '&lt;': 'lt', '&gt;': 'gt', '=': 'eq'}
        self.unaryOp = {'-': 'neg', '~': 'not'}
        self.ifCounter = -1
        self.whileCounter = -1
        self.parameters = 0
        self.currentSubroutine = ''
        self.advance()
        self.CompileClass()

    def advance(self):
        if self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

    def CompileClass(self):

        # class
        if not(self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.CLASS):
            raise Exception('Expected class')

        # className
        self.advance()
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.className = self.tokenizer.identifier()
        else:
            raise Exception('Expected className')

        # {
        self.advance()
        if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{'):
            raise Exception('Expected {')

        self.advance()
        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != '}':
            if self.tokenizer.tokenType() == TokenType.KEYWORD:
                keyword = self.tokenizer.keyWord()
                if keyword in (KeyWord.STATIC, KeyWord.FIELD):
                    self.CompileClassVarDec()
                if keyword in (KeyWord.CONSTRUCTOR, KeyWord.FUNCTION, KeyWord.METHOD):
                    self.CompileSubroutineDec()
            else:
                raise Exception('Expected classVarDec or subroutineDec')

    def CompileClassVarDec(self):

        # static/field
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.STATIC, KeyWord.FIELD):
            segment = self.tokenizer.keyWord()
        else:
            raise Exception('Expected static/field')

        # type
        self.advance()
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.INT, KeyWord.CHAR, KeyWord.BOOLEAN)) or \
                (self.tokenizer.tokenType() == TokenType.IDENTIFIER):
            fieldType = self.tokenizer.identifier()
        else:
            raise Exception('Expected type')

        while not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            self.advance()

            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.symbolTable.define(
                    self.tokenizer.identifier(), fieldType, segment)
            else:
                raise Exception('Expected varName')

            # , or ;
            self.advance()
            if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in (',', ';')):
                raise Exception('Expected , or ;')

        self.advance()

    def CompileSubroutineDec(self):
        self.ifCounter = -1
        self.whileCounter = -1
        # constructor/function/method
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.CONSTRUCTOR, KeyWord.FUNCTION, KeyWord.METHOD):
            self.subroutineType = self.tokenizer.keyWord()
        else:
            raise Exception('Expected constructor/function/method')

        self.symbolTable.startSubroutine()

        # void/type
        self.advance()
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.VOID, KeyWord.INT, KeyWord.CHAR, KeyWord.BOOLEAN)) or \
                self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.subroutineReturnType = self.tokenizer.identifier()
        else:
            raise Exception('Expected void/type')

        # subroutineName
        self.advance()
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.currentSubroutine = self.tokenizer.identifier()
        else:
            raise Exception('Expected subroutineName')

        # (
        self.advance()
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '('):
            raise Exception('Expected (')

        self.advance()
        self.compileParameterList()

        # )
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')'):
            raise Exception('Expected )')

        # {
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
            self.compileSubroutineBody()
        else:
            raise Exception('Expected {')

    def compileParameterList(self):
        self.parameters = 0
        if self.subroutineType == KeyWord.METHOD:
            self.symbolTable.define('this', self.className, KeyWordArg.ARG)
        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != ')':

            # type
            if self.tokenizer.tokenType() == TokenType.KEYWORD or self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                parameterType = self.tokenizer.tokenType()
            else:
                raise Exception('Expected type')

            self.advance()
            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                varName = self.tokenizer.identifier()
                self.symbolTable.define(varName, parameterType, KeyWordArg.ARG)
                self.parameters += 1
            else:
                raise Exception('Expected identifier')

            self.advance()
            # , or ;
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in (',', ')'):
                if self.tokenizer.symbol() == ',':
                    self.advance()
            else:
                raise Exception('Expected , or )')

    def compileSubroutineBody(self):

        # {
        if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{'):
            raise Exception('Expected {')

        # varDec
        self.advance()
        while self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.VAR:
            self.compileVarDec()

        self.vmWriter.writeFunction(
            self.className + '.' + self.currentSubroutine, self.symbolTable.varCount(KeyWord.VAR))
        if self.subroutineType == KeyWord.CONSTRUCTOR:
            self.vmWriter.writePush(
                'constant', self.symbolTable.varCount(KeyWord.FIELD))
            self.vmWriter.writeCall('Memory.alloc', 1)
            self.vmWriter.writePop('pointer', 0)
        if self.subroutineType == KeyWord.METHOD:
            self.vmWriter.writePush('argument', 0)
            self.vmWriter.writePop('pointer', 0)

        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != '}':
            if self.tokenizer.keyWord() in (KeyWord.LET, KeyWord.IF, KeyWord.WHILE, KeyWord.DO, KeyWord.RETURN):
                self.compileStatements()
            else:
                raise Exception('Expected var/let/if/while/do/return')

        self.advance()

    def compileVarDec(self):

        # var
        if not (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.VAR):
            raise Exception('Expected var')

        # type
        self.advance()
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.INT, KeyWord.CHAR, KeyWord.BOOLEAN)) or \
                self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            varType = self.tokenizer.identifier()
        else:
            raise Exception('Expected type')

        while not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            self.advance()
            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.symbolTable.define(
                    self.tokenizer.identifier(), varType, KeyWord.VAR)
            else:
                raise Exception('Expected identifier')

            # , or ;
            self.advance()
            if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in (',', ';')):
                raise Exception('Expected , or ;')

        self.advance()

    def compileStatements(self):
        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != '}':
            if self.tokenizer.tokenType() == TokenType.KEYWORD:
                if self.tokenizer.keyWord() == KeyWord.LET:
                    self.compileLet()
                elif self.tokenizer.keyWord() == KeyWord.IF:
                    self.compileIf()
                elif self.tokenizer.keyWord() == KeyWord.WHILE:
                    self.compileWhile()
                elif self.tokenizer.keyWord() == KeyWord.DO:
                    self.compileDo()
                elif self.tokenizer.keyWord() == KeyWord.RETURN:
                    self.compileReturn()
                else:
                    raise Exception('Expected let/if/while/do/return')
            else:
                raise Exception('Expected keyword')

    def compileLet(self):
        # let
        if not (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.LET):
            raise Exception('Expected let')

        self.advance()
        # varName
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            varName = self.tokenizer.identifier()
            varType = self.symbolTable.kindOf(varName).value
            varIndex = self.symbolTable.indexOf(varName)
        else:
            raise Exception('Expected identifier')

        array = False
        # [
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '[':
            self.advance()
            # expression
            self.CompileExpression()
            self.vmWriter.writePush(varType, varIndex)
            self.vmWriter.writeArithmetic('add')
            array = True
            # ]
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ']':
                self.advance()
            else:
                raise Exception('Expected ]')

        # =
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '=':
            self.advance()
            # expression
            self.CompileExpression()
            if array:
                self.vmWriter.writePop('temp', 0)
                self.vmWriter.writePop('pointer', 1)
                self.vmWriter.writePush('temp', 0)
                self.vmWriter.writePop('that', 0)
            else:
                self.vmWriter.writePop(varType, varIndex)

        else:
            raise Exception('Expected =')

        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            raise Exception('Expected ;')

        self.advance()

    def compileIf(self):
        self.ifCounter += 1
        current_counter = self.ifCounter
        if not (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.IF):
            raise Exception('Expected if')

        # (
        self.advance()
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '('):
            raise Exception('Expected (')

        # expression
        self.advance()
        self.CompileExpression()
        self.vmWriter.writeIf('IF_TRUE' + str(current_counter))
        self.vmWriter.writeGoto('IF_FALSE' + str(current_counter))
        self.vmWriter.writeLabel('IF_TRUE' + str(current_counter))

        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')'):
            raise Exception('Expected )')

        # {
        self.advance()
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{'):
            raise Exception('Expected {')

        self.advance()
        self.compileStatements()

        # }
        if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '}'):
            raise Exception('Expected }')

        self.advance()
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.ELSE:
            self.vmWriter.writeGoto('IF_END' + str(current_counter))
        self.vmWriter.writeLabel('IF_FALSE' + str(current_counter))
        # else

        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.ELSE:
            self.advance()
            # {
            if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{'):
                raise Exception('Expected {')
            self.advance()
            self.compileStatements()
            self.vmWriter.writeLabel('IF_END' + str(current_counter))
            # }
            if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '}'):
                raise Exception('Expected }')
            self.advance()

    def compileWhile(self):
        self.whileCounter += 1
        current_counter = self.whileCounter

        # while
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.WHILE):
            self.vmWriter.writeLabel('WHILE_EXP' + str(current_counter))
        else:
            raise Exception('Expected while')

        # (
        self.advance()
        if not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '('):
            raise Exception('Expected (')

        # expression
        self.advance()
        self.CompileExpression()
        self.vmWriter.writeArithmetic('not')
        self.vmWriter.writeIf('WHILE_END' + str(current_counter))
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')'):
            raise Exception('Expected )')

        # {
        self.advance()
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{'):
            raise Exception('Expected {')

        self.advance()
        self.compileStatements()
        self.vmWriter.writeGoto('WHILE_EXP' + str(current_counter))
        self.vmWriter.writeLabel('WHILE_END' + str(current_counter))
        # }
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '}'):
            raise Exception('Expected }')

        self.advance()

    def compileDo(self):
        # do
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.DO:
            self.advance()
        else:
            raise Exception('Expected do')

        # className|subroutineName
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            identifier1 = self.tokenizer.identifier()
        else:
            raise Exception('Expected identifier')

        class_dot_method = False
        # .
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '.':
            # subroutineName
            self.advance()
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                identifier2 = self.tokenizer.identifier()
                self.advance()
                class_dot_method = True
            else:
                raise Exception('Expected identifier')

        # (
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
            self.advance()
        else:
            raise Exception('Expected (')

        # expressionList
        if self.symbolTable.typeOf(identifier1):
            if self.symbolTable.kindOf(identifier1) == KeyWord.FIELD:
                self.vmWriter.writePush(
                    'this', self.symbolTable.indexOf(identifier1))
            else:
                self.vmWriter.writePush(
                    'local', self.symbolTable.indexOf(identifier1))
            identifier1 = self.symbolTable.typeOf(identifier1)
            self.CompileExpressionList()
            self.parameters += 1
            self.vmWriter.writeCall(
                '.'.join([identifier1, identifier2]), self.parameters)
        elif class_dot_method:
            self.CompileExpressionList()
            self.vmWriter.writeCall(
                '.'.join([identifier1, identifier2]), self.parameters)
        else:
            self.vmWriter.writePush('pointer', 0)
            self.CompileExpressionList()
            self.vmWriter.writeCall(
                '.'.join([self.className, identifier1]), self.parameters + 1)
        self.vmWriter.writePop('temp', 0)
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
            self.advance()
        else:
            raise Exception('Expected )')
        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            raise Exception('Expected ;')
        self.advance()

    def compileReturn(self):

        self.advance()
        if self.tokenizer.symbol() != ';':
            self.CompileExpression()
        else:
            self.vmWriter.writePush('constant', 0)
        self.vmWriter.writeReturn()

        if not(self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            raise Exception('Expected ;')

        self.advance()

    def CompileExpression(self):
        self.CompileTerm()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in self.op:
            operator = self.tokenizer.symbol()
            self.advance()
            self.CompileTerm()
            self.vmWriter.writeArithmetic(self.op[operator])

    def CompileTerm(self):
        # integerConstant
        if self.tokenizer.tokenType() == TokenType.INT_CONST:
            self.vmWriter.writePush('constant', self.tokenizer.intVal())
            self.advance()
        elif self.tokenizer.tokenType() == TokenType.STRING_CONST:
            self.vmWriter.writePush(
                'constant', len(self.tokenizer.stringVal()))
            self.vmWriter.writeCall('String.new', 1)
            stringVal = self.tokenizer.stringVal()
            for c in stringVal:
                self.vmWriter.writePush('constant', ord(c))
                self.vmWriter.writeCall('String.appendChar', 2)

            self.advance()
        elif self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.FALSE, KeyWord.NULL):

            self.vmWriter.writePush(
                'constant', self.tokenizer.keyWord().value)
            self.advance()
        elif self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.TRUE:
            self.vmWriter.writePush(
                'constant', 0)
            self.vmWriter.writeArithmetic('not')
            self.advance()
        elif self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.THIS:
            self.vmWriter.writePush(
                'pointer', 0)
            self.advance()
        elif self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            identifier1 = self.tokenizer.identifier()
            self.advance()
            # [
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '[':
                self.advance()
                self.CompileExpression()
                self.vmWriter.writePush(self.symbolTable.kindOf(
                    identifier1).value, self.symbolTable.indexOf(identifier1))
                self.vmWriter.writeArithmetic('add')
                self.vmWriter.writePop('pointer', 1)
                self.vmWriter.writePush('that', 0)
                if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ']':
                    self.advance()
                else:
                    raise Exception('Expected ]')
            elif self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '.':
                self.advance()
                if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                    identifier2 = self.tokenizer.identifier()
                    self.advance()
                else:
                    raise Exception('Expected identifier')
                if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
                    self.advance()
                    self.CompileExpressionList()
                    if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
                        self.advance()
                    else:
                        raise Exception('Expected )')
                else:
                    raise Exception('Expected (')
                if self.symbolTable.typeOf(identifier1):
                    if self.symbolTable.kindOf(identifier1) == KeyWord.FIELD:
                        self.vmWriter.writePush(
                            'this', self.symbolTable.indexOf(identifier1))
                    else:
                        self.vmWriter.writePush(
                            'local', self.symbolTable.indexOf(identifier1))
                    identifier1 = self.symbolTable.typeOf(identifier1)
                    self.parameters += 1
                self.vmWriter.writeCall(
                    '.'.join([identifier1, identifier2]), self.parameters)
            else:
                self.vmWriter.writePush(
                    self.symbolTable.kindOf(identifier1).value, self.symbolTable.indexOf(identifier1))
        elif (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in self.unaryOp.keys()):
            operator = self.tokenizer.symbol()
            self.advance()
            if (self.tokenizer.tokenType() in (TokenType.IDENTIFIER, TokenType.INT_CONST)):
                self.CompileTerm()
            elif (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '('):
                self.advance()
                self.CompileExpression()
                if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
                    self.advance()
                else:
                    raise Exception('Expected )')
            else:
                raise Exception('Expected term or expression')
            self.vmWriter.writeArithmetic(self.unaryOp[operator])
        elif self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
            self.advance()
            self.CompileExpression()
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
                self.advance()
            else:
                raise Exception('Expected )')

    def CompileExpressionList(self):
        self.parameters = 0
        while self.tokenizer.tokenType() != TokenType.SYMBOL or self.tokenizer.symbol() != ')':
            self.CompileExpression()
            self.parameters += 1
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ',':
                self.advance()
