
import re
from enum import Enum


class TokenType(Enum):
    KEYWORD = 1
    SYMBOL = 2
    IDENTIFIER = 3
    INT_CONST = 4
    STRING_CONST = 5


class KeyWord(Enum):
    CLASS = 0
    METHOD = 1
    FUNCTION = 2
    CONSTRUCTOR = 3
    INT = 4
    BOOLEAN = 5
    CHAR = 6
    VOID = 7
    VAR = 8
    STATIC = 9
    FIELD = 10
    LET = 11
    DO = 12
    IF = 13
    ELSE = 14
    WHILE = 15
    RETURN = 16
    TRUE = 17
    FALSE = 18
    NULL = 19
    THIS = 20


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
        match self.current_token:
            case 'class':
                return KeyWord.CLASS
            case 'constructor':
                return KeyWord.CONSTRUCTOR
            case 'function':
                return KeyWord.FUNCTION
            case 'method':
                return KeyWord.METHOD
            case 'field':
                return KeyWord.FIELD
            case 'static':
                return KeyWord.STATIC
            case 'var':
                return KeyWord.VAR
            case 'int':
                return KeyWord.INT
            case 'char':
                return KeyWord.CHAR
            case 'boolean':
                return KeyWord.BOOLEAN
            case 'void':
                return KeyWord.VOID
            case 'true':
                return KeyWord.TRUE
            case 'false':
                return KeyWord.FALSE
            case 'null':
                return KeyWord.NULL
            case 'this':
                return KeyWord.THIS
            case 'let':
                return KeyWord.LET
            case 'do':
                return KeyWord.DO
            case 'if':
                return KeyWord.IF
            case 'else':
                return KeyWord.ELSE
            case 'while':
                return KeyWord.WHILE
            case 'return':
                return KeyWord.RETURN
            case default:
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
