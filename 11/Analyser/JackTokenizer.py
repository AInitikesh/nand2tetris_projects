
import re
from enum import Enum


class TokenType(Enum):
    KEYWORD = 'keyword'
    SYMBOL = 'symbol'
    IDENTIFIER = 'identifier'
    INT_CONST = 'integerConstant'
    STRING_CONST = 'stringConstant'


class KeyWord(Enum):
    CLASS = 'class'
    METHOD = 'method'
    FUNCTION = 'function'
    CONSTRUCTOR = 'constructor'
    INT = 'int'
    BOOLEAN = 'boolean'
    CHAR = 'char'
    VOID = 'void'
    VAR = 'local'
    STATIC = 'static'
    FIELD = 'this'
    LET = 'let'
    DO = 'do'
    IF = 'if'
    ELSE = 'else'
    WHILE = 'while'
    RETURN = 'return'
    TRUE = -1
    FALSE = 0
    NULL = 0
    THIS = 'this'


class JackTokenizer:

    def __init__(self, input_file):

        self.keywords = {'class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char',
                         'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return'}
        self.symbols = {'{', '}', '(', ')', '[', ']', '.', ',',
                        ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'}
        self.tokens = []
        with open(input_file, 'r') as file:
            self.extractTokens(file)
        self.current_token_no = -1
        self.current_token = None

    def extractTokens(self, file):
        comment_section = False
        for line in file.readlines():
            line = line.strip()
            if line.startswith('/*') and not comment_section:
                if not line.endswith('*/'):
                    comment_section = True
                continue
            if line.endswith('*/'):
                comment_section = False
                continue
            if line.startswith('//') or comment_section:
                continue
            else:
                line = line.split('//')[0]
                line = line.strip()
                if line != '':
                    self.tokenize(line)

    def tokenize(self, line):
        curr_token = ''
        stringSeq = False
        for char in line:
            if char == '"':
                stringSeq = not stringSeq
            elif char == ' ' and not stringSeq:
                curr_token = curr_token.strip()
                if curr_token != '':
                    self.tokens.append(curr_token)
                curr_token = ''
            elif char in self.symbols and not stringSeq:
                curr_token = curr_token.strip()
                if curr_token != '':
                    self.tokens.append(curr_token)
                self.tokens.append(char)
                curr_token = ''
                continue
            curr_token += char

    def hasMoreTokens(self):
        return self.current_token_no < (len(self.tokens) - 1)

    def advance(self):
        self.current_token_no += 1
        self.current_token = self.tokens[self.current_token_no]

    def tokenType(self):
        if self.current_token in self.keywords:
            return TokenType.KEYWORD
        elif self.current_token in self.symbols:
            return TokenType.SYMBOL
        elif self.current_token.isdigit():
            return TokenType.INT_CONST
        elif self.current_token.startswith('"') and self.current_token.endswith('"'):
            return TokenType.STRING_CONST
        elif re.match('^[a-zA-Z_][a-zA-Z0-9_]*', self.current_token):
            return TokenType.IDENTIFIER
        else:
            raise Exception('Invalid token: ' + self.current_token)

    def keyWord(self):
        if self.current_token == 'class':
            return KeyWord.CLASS
        if self.current_token == 'constructor':
            return KeyWord.CONSTRUCTOR
        if self.current_token == 'function':
            return KeyWord.FUNCTION
        if self.current_token == 'method':
            return KeyWord.METHOD
        if self.current_token == 'field':
            return KeyWord.FIELD
        if self.current_token == 'static':
            return KeyWord.STATIC
        if self.current_token == 'var':
            return KeyWord.VAR
        if self.current_token == 'int':
            return KeyWord.INT
        if self.current_token == 'char':
            return KeyWord.CHAR
        if self.current_token == 'boolean':
            return KeyWord.BOOLEAN
        if self.current_token == 'void':
            return KeyWord.VOID
        if self.current_token == 'true':
            return KeyWord.TRUE
        if self.current_token == 'false':
            return KeyWord.FALSE
        if self.current_token == 'null':
            return KeyWord.NULL
        if self.current_token == 'this':
            return KeyWord.THIS
        if self.current_token == 'let':
            return KeyWord.LET
        if self.current_token == 'do':
            return KeyWord.DO
        if self.current_token == 'if':
            return KeyWord.IF
        if self.current_token == 'else':
            return KeyWord.ELSE
        if self.current_token == 'while':
            return KeyWord.WHILE
        if self.current_token == 'return':
            return KeyWord.RETURN
        else:
            raise Exception('Invalid keyword: ' + self.current_token)

    def symbol(self):
        if self.current_token == '<':
            return '&lt;'
        elif self.current_token == '>':
            return '&gt;'
        elif self.current_token == '&':
            return '&amp;'
        elif self.current_token == '"':
            return '&quot;'
        else:
            return self.current_token

    def identifier(self):
        return self.current_token

    def intVal(self):
        return self.current_token

    def stringVal(self):
        return self.current_token.replace('"', '')
