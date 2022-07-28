from JackTokenizer import JackTokenizer, TokenType, KeyWord


class CompilationEngine:

    def __init__(self, input_file, output_file):
        self.tokenizer = JackTokenizer(input_file)
        self.output_file = open(output_file, 'w')
        self.indent = 0
        self.advance()
        self.CompileClass()

    def write(self, text):
        indentation = ' ' * self.indent * 2
        self.output_file.write(indentation + text + '\n')

    def __del__(self):
        self.output_file.close()

    def advance(self):
        if self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

    def openTag(self, tag):
        self.write(f'<{tag}>')
        self.indent += 1

    def closeTag(self, tag):
        self.indent -= 1
        self.write(f'</{tag}>')

    def writeToken(self):
        tokenType = self.tokenizer.tokenType()
        match tokenType:
            case TokenType.KEYWORD:
                keyword = self.tokenizer.keyWord()
                match keyword:
                    case KeyWord.CLASS:
                        self.write('<keyword> class </keyword>')
                    case KeyWord.CONSTRUCTOR:
                        self.write('<keyword> constructor </keyword>')
                    case KeyWord.FUNCTION:
                        self.write('<keyword> function </keyword>')
                    case KeyWord.METHOD:
                        self.write('<keyword> method </keyword>')
                    case KeyWord.INT:
                        self.write('<keyword> int </keyword>')
                    case KeyWord.BOOLEAN:
                        self.write('<keyword> boolean </keyword>')
                    case KeyWord.CHAR:
                        self.write('<keyword> char </keyword>')
                    case KeyWord.VOID:
                        self.write('<keyword> void </keyword>')
                    case KeyWord.FIELD:
                        self.write('<keyword> field </keyword>')
                    case KeyWord.STATIC:
                        self.write('<keyword> static </keyword>')
                    case KeyWord.LET:
                        self.write('<keyword> let </keyword>')
                    case KeyWord.DO:
                        self.write('<keyword> do </keyword>')
                    case KeyWord.IF:
                        self.write('<keyword> if </keyword>')
                    case KeyWord.ELSE:
                        self.write('<keyword> else </keyword>')
                    case KeyWord.WHILE:
                        self.write('<keyword> while </keyword>')
                    case KeyWord.RETURN:
                        self.write('<keyword> return </keyword>')
                    case KeyWord.TRUE:
                        self.write('<keyword> true </keyword>')
                    case KeyWord.FALSE:
                        self.write('<keyword> false </keyword>')
                    case KeyWord.NULL:
                        self.write('<keyword> null </keyword>')
                    case KeyWord.THIS:
                        self.write('<keyword> this </keyword>')
                    case KeyWord.VAR:
                        self.write('<keyword> var </keyword>')
            case TokenType.SYMBOL:
                symbol = self.tokenizer.symbol()
                self.write('<symbol> ' + symbol + ' </symbol>')
            case TokenType.IDENTIFIER:
                identifier = self.tokenizer.identifier()
                self.write('<identifier> ' + identifier + ' </identifier>')
            case TokenType.INT_CONST:
                intVal = self.tokenizer.intVal()
                self.write('<integerConstant> ' +
                           intVal + ' </integerConstant>')
            case TokenType.STRING_CONST:
                stringVal = self.tokenizer.stringVal()
                self.write('<stringConstant> ' +
                           stringVal + ' </stringConstant>')

    def CompileClass(self):
        tag = 'class'
        self.openTag(tag)

        # class
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.CLASS:
            self.writeToken()
        else:
            raise Exception('Expected class')

        # className
        self.advance()
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.writeToken()
        else:
            raise Exception('Expected className')

        # {
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
            self.writeToken()
        else:
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

        self.writeToken()
        self.closeTag(tag)

    def CompileClassVarDec(self):
        tag = 'classVarDec'
        self.openTag(tag)

        # static/field
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.STATIC, KeyWord.FIELD):
            self.writeToken()
        else:
            raise Exception('Expected static/field')

        # type
        self.advance()
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.INT, KeyWord.CHAR, KeyWord.BOOLEAN)) or \
                (self.tokenizer.tokenType() == TokenType.IDENTIFIER):
            self.writeToken()
        else:
            raise Exception('Expected type')

        while not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            self.advance()

            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.writeToken()
            else:
                raise Exception('Expected varName')

            # , or ;
            self.advance()
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in (',', ';'):
                self.writeToken()
            else:
                raise Exception('Expected , or ;')

        self.advance()
        self.closeTag(tag)

    def CompileSubroutineDec(self):
        tag = 'subroutineDec'
        self.openTag(tag)

        # constructor/function/method
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.CONSTRUCTOR, KeyWord.FUNCTION, KeyWord.METHOD):
            self.writeToken()
        else:
            raise Exception('Expected constructor/function/method')

        # void/type
        self.advance()
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.VOID, KeyWord.INT, KeyWord.CHAR, KeyWord.BOOLEAN)) or \
                self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.writeToken()
        else:
            raise Exception('Expected void/type')

        # subroutineName
        self.advance()
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.writeToken()
        else:
            raise Exception('Expected subroutineName')

        # (
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
            self.writeToken()
        else:
            raise Exception('Expected (')

        self.advance()
        self.compileParameterList()

        # )
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
            self.writeToken()

        # {
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
            self.compileSubroutineBody()
        else:
            raise Exception('Expected {')

        self.closeTag(tag)

    def compileParameterList(self):
        tag = 'parameterList'
        self.openTag(tag)

        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != ')':

            # type
            if self.tokenizer.tokenType() == TokenType.KEYWORD:
                self.writeToken()
            else:
                raise Exception('Expected type')

            self.advance()
            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.writeToken()
            else:
                raise Exception('Expected identifier')

            self.advance()
            # , or ;
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in (',', ')'):
                if self.tokenizer.symbol() == ',':
                    self.writeToken()
                    self.advance()
            else:
                raise Exception('Expected , or )')

        self.closeTag(tag)

    def compileSubroutineBody(self):
        tag = 'subroutineBody'
        self.openTag(tag)

        # {
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
            self.writeToken()

        # varDec
        self.advance()
        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != '}':
            if self.tokenizer.tokenType() == TokenType.KEYWORD:
                if self.tokenizer.keyWord() == KeyWord.VAR:
                    self.compileVarDec()
                elif self.tokenizer.keyWord() in (KeyWord.LET, KeyWord.IF, KeyWord.WHILE, KeyWord.DO, KeyWord.RETURN):
                    self.compileStatements()
                else:
                    raise Exception('Expected var/let/if/while/do/return')
            else:
                raise Exception('Expected keyword')
        self.writeToken()
        self.advance()
        self.closeTag(tag)

    def compileVarDec(self):
        tag = 'varDec'
        self.openTag(tag)

        # var
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.VAR:
            self.writeToken()
        else:
            raise Exception('Expected var')

        # type
        self.advance()
        if (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.INT, KeyWord.CHAR, KeyWord.BOOLEAN)) or \
                self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.writeToken()

        while not (self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';'):
            self.advance()

            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.writeToken()
            else:
                raise Exception('Expected identifier')

            # , or ;
            self.advance()
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() in (',', ';'):
                self.writeToken()
            else:
                raise Exception('Expected , or ;')

        self.advance()
        self.closeTag(tag)

    def compileStatements(self):
        tag = 'statements'
        self.openTag(tag)

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

        self.closeTag(tag)

    def compileLet(self):
        tag = 'letStatement'
        self.openTag(tag)

        # let
        self.writeToken()

        self.advance()
        while self.tokenizer.tokenType() != TokenType.SYMBOL and self.tokenizer.symbol() != ';':
            # varName
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.writeToken()
            else:
                raise Exception('Expected identifier')

            # [
            self.advance()
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '[':
                self.writeToken()
                self.advance()
                # expression
                self.CompileExpression()
                # ]
                if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ']':
                    self.writeToken()
                    self.advance()
                else:
                    raise Exception('Expected ]')

            # =
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '=':
                self.writeToken()

                self.advance()
                # expression
                self.CompileExpression()
            else:
                raise Exception('Expected =')

        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';':
            self.writeToken()
        else:
            raise Exception('Expected ;')

        self.advance()
        self.closeTag(tag)

    def compileIf(self):
        tag = 'ifStatement'
        self.openTag(tag)

        # if
        self.writeToken()

        # (
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
            self.writeToken()
        else:
            raise Exception('Expected (')

        # expression
        self.advance()
        self.CompileExpression()

        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
            self.writeToken()
        else:
            raise Exception('Expected )')

        # {
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
            self.writeToken()
        else:
            raise Exception('Expected {')

        self.advance()
        self.compileStatements()

        # }
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '}':
            self.writeToken()

        # else
        self.advance()
        if self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() == KeyWord.ELSE:
            self.writeToken()
            self.advance()
            # {
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
                self.writeToken()
            else:
                raise Exception('Expected {')
            self.advance()
            self.compileStatements()
            # }
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '}':
                self.writeToken()
                self.advance()
            else:
                raise Exception('Expected }')

        self.closeTag(tag)

    def compileWhile(self):
        tag = 'whileStatement'
        self.openTag(tag)

        # while
        self.writeToken()

        # (
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
            self.writeToken()
        else:
            raise Exception('Expected (')

        # expression
        self.advance()
        self.CompileExpression()

        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
            self.writeToken()
        else:
            raise Exception('Expected )')

        # {
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '{':
            self.writeToken()
        else:
            raise Exception('Expected {')

        self.advance()
        self.compileStatements()

        # }
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '}':
            self.writeToken()

        self.advance()
        self.closeTag(tag)

    def compileDo(self):
        tag = 'doStatement'
        self.openTag(tag)

        # do
        self.writeToken()

        # className|subroutineName
        self.advance()
        if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
            self.writeToken()
        else:
            raise Exception('Expected identifier')

        # .
        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '.':
            self.writeToken()
            # subroutineName
            self.advance()
            if self.tokenizer.tokenType() == TokenType.IDENTIFIER:
                self.writeToken()
                self.advance()
            else:
                raise Exception('Expected identifier')

        # (
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == '(':
            self.writeToken()
        else:
            raise Exception('Expected (')

        # expressionList
        self.advance()
        self.CompileExpressionList()

        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ')':
            self.writeToken()
        else:
            raise Exception('Expected )')

        self.advance()
        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';':
            self.writeToken()
        else:
            raise Exception('Expected ;')

        self.advance()
        self.closeTag(tag)

    def compileReturn(self):
        tag = 'returnStatement'
        self.openTag(tag)

        # return
        self.writeToken()

        self.advance()
        if self.tokenizer.symbol() != ';':
            self.CompileExpression()

        if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ';':
            self.writeToken()
        else:
            raise Exception('Expected ;')

        self.advance()
        self.closeTag(tag)

    def CompileExpression(self):
        tag = 'expression'
        self.openTag(tag)
        self.CompileTerm()
        self.closeTag(tag)

    def CompileTerm(self):
        tag = 'term'
        self.openTag(tag)

        # integerConstant
        if self.tokenizer.tokenType() in (TokenType.INT_CONST, TokenType.STRING_CONST, TokenType.IDENTIFIER) or \
                (self.tokenizer.tokenType() == TokenType.KEYWORD and self.tokenizer.keyWord() in (KeyWord.TRUE, KeyWord.FALSE, KeyWord.NULL, KeyWord.THIS)):
            self.writeToken()
            self.advance()

        self.closeTag(tag)

    def CompileExpressionList(self):
        tag = 'expressionList'
        self.openTag(tag)
        while self.tokenizer.tokenType() != TokenType.SYMBOL or self.tokenizer.symbol() != ')':
            self.CompileExpression()
            if self.tokenizer.tokenType() == TokenType.SYMBOL and self.tokenizer.symbol() == ',':
                self.writeToken()
                self.advance()
        self.closeTag(tag)
