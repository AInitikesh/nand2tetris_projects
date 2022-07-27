
// C_PUSH constant 3030
@3030 // 0
D=A // 1
@SP // 2
A=M // 3
M=D // 4
@SP // 5
M=M+1 // 6
// C_POP pointer 0
@SP // 7
M=M-1 // 8
A=M // 9
D=M // 10
@THIS // 11
M=D // 12
// C_PUSH constant 3040
@3040 // 13
D=A // 14
@SP // 15
A=M // 16
M=D // 17
@SP // 18
M=M+1 // 19
// C_POP pointer 1
@SP // 20
M=M-1 // 21
A=M // 22
D=M // 23
@THAT // 24
M=D // 25
// C_PUSH constant 32
@32 // 26
D=A // 27
@SP // 28
A=M // 29
M=D // 30
@SP // 31
M=M+1 // 32
// C_POP this 2
@2 // 33
D=A // 34
@THIS // 35
D=M+D // 36
@R13 // 37
M=D // 38
@SP // 39
M=M-1 // 40
A=M // 41
D=M // 42
@R13 // 43
A=M // 44
M=D // 45
// C_PUSH constant 46
@46 // 46
D=A // 47
@SP // 48
A=M // 49
M=D // 50
@SP // 51
M=M+1 // 52
// C_POP that 6
@6 // 53
D=A // 54
@THAT // 55
D=M+D // 56
@R13 // 57
M=D // 58
@SP // 59
M=M-1 // 60
A=M // 61
D=M // 62
@R13 // 63
A=M // 64
M=D // 65
// C_PUSH pointer 0
@THIS // 66
D=M // 67
@SP // 68
A=M // 69
M=D // 70
@SP // 71
M=M+1 // 72
// C_PUSH pointer 1
@THAT // 73
D=M // 74
@SP // 75
A=M // 76
M=D // 77
@SP // 78
M=M+1 // 79
// add
@SP // 80
M=M-1 // 81
@SP // 82
A=M // 83
D=M // 84
@SP // 85
M=M-1 // 86
@SP // 87
A=M // 88
M=M+D // 89
@SP // 90
M=M+1 // 91
// C_PUSH this 2
@2 // 92
D=A // 93
@THIS // 94
A=M+D // 95
D=M // 96
@SP // 97
A=M // 98
M=D // 99
@SP // 100
M=M+1 // 101
// sub
@SP // 102
M=M-1 // 103
@SP // 104
A=M // 105
D=M // 106
@SP // 107
M=M-1 // 108
@SP // 109
A=M // 110
M=M-D // 111
@SP // 112
M=M+1 // 113
// C_PUSH that 6
@6 // 114
D=A // 115
@THAT // 116
A=M+D // 117
D=M // 118
@SP // 119
A=M // 120
M=D // 121
@SP // 122
M=M+1 // 123
// add
@SP // 124
M=M-1 // 125
@SP // 126
A=M // 127
D=M // 128
@SP // 129
M=M-1 // 130
@SP // 131
A=M // 132
M=M+D // 133
@SP // 134
M=M+1 // 135