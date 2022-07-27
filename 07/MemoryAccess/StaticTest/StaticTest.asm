
// C_PUSH constant 111
@111 // 0
D=A // 1
@SP // 2
A=M // 3
M=D // 4
@SP // 5
M=M+1 // 6
// C_PUSH constant 333
@333 // 7
D=A // 8
@SP // 9
A=M // 10
M=D // 11
@SP // 12
M=M+1 // 13
// C_PUSH constant 888
@888 // 14
D=A // 15
@SP // 16
A=M // 17
M=D // 18
@SP // 19
M=M+1 // 20
// C_POP static 8
@SP // 21
M=M-1 // 22
A=M // 23
D=M // 24
@StaticTest.8 // 25
M=D // 26
// C_POP static 3
@SP // 27
M=M-1 // 28
A=M // 29
D=M // 30
@StaticTest.3 // 31
M=D // 32
// C_POP static 1
@SP // 33
M=M-1 // 34
A=M // 35
D=M // 36
@StaticTest.1 // 37
M=D // 38
// C_PUSH static 3
@StaticTest.3 // 39
D=M // 40
@SP // 41
A=M // 42
M=D // 43
@SP // 44
M=M+1 // 45
// C_PUSH static 1
@StaticTest.1 // 46
D=M // 47
@SP // 48
A=M // 49
M=D // 50
@SP // 51
M=M+1 // 52
// sub
@SP // 53
M=M-1 // 54
@SP // 55
A=M // 56
D=M // 57
@SP // 58
M=M-1 // 59
@SP // 60
A=M // 61
M=M-D // 62
@SP // 63
M=M+1 // 64
// C_PUSH static 8
@StaticTest.8 // 65
D=M // 66
@SP // 67
A=M // 68
M=D // 69
@SP // 70
M=M+1 // 71
// add
@SP // 72
M=M-1 // 73
@SP // 74
A=M // 75
D=M // 76
@SP // 77
M=M-1 // 78
@SP // 79
A=M // 80
M=M+D // 81
@SP // 82
M=M+1 // 83