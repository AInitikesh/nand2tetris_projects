
class VMWriter:

    def __init__(self, output_file) -> None:
        self.file = open(output_file, 'w')

    def writeLine(self, *line) -> None:
        self.file.write(" ".join(line) + '\n')

    def __del__(self):
        self.file.close()

    def writePush(self, segment, index) -> None:
        self.writeLine('push', segment, str(index))

    def writePop(self, segment, index) -> None:
        self.writeLine('pop', segment, str(index))

    def writeArithmetic(self, command) -> None:
        self.writeLine(command)

    def writeLabel(self, label) -> None:
        self.writeLine('label', label)

    def writeGoto(self, label) -> None:
        self.writeLine('goto', label)

    def writeIf(self, label) -> None:
        self.writeLine('if-goto', label)

    def writeCall(self, name, nargs) -> None:
        self.writeLine('call', name, str(nargs))

    def writeFunction(self, name, nlocals) -> None:
        self.writeLine('function', name, str(nlocals))

    def writeReturn(self) -> None:
        self.writeLine('return')

    def close(self) -> None:
        self.file.close()
