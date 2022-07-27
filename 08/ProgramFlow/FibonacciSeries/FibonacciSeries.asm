
// C_PUSH argument 1
	@1 // 0
	D=A // 1
	@ARG // 2
	A=M+D // 3
	D=M // 4
	@SP // 5
	A=M // 6
	M=D // 7
	@SP // 8
	M=M+1 // 9
// C_POP pointer 1
	@SP // 10
	M=M-1 // 11
	A=M // 12
	D=M // 13
	@THAT // 14
	M=D // 15
// C_PUSH constant 0
	@0 // 16
	D=A // 17
	@SP // 18
	A=M // 19
	M=D // 20
	@SP // 21
	M=M+1 // 22
// C_POP that 0
	@0 // 23
	D=A // 24
	@THAT // 25
	D=M+D // 26
	@R13 // 27
	M=D // 28
	@SP // 29
	M=M-1 // 30
	A=M // 31
	D=M // 32
	@R13 // 33
	A=M // 34
	M=D // 35
// C_PUSH constant 1
	@1 // 36
	D=A // 37
	@SP // 38
	A=M // 39
	M=D // 40
	@SP // 41
	M=M+1 // 42
// C_POP that 1
	@1 // 43
	D=A // 44
	@THAT // 45
	D=M+D // 46
	@R13 // 47
	M=D // 48
	@SP // 49
	M=M-1 // 50
	A=M // 51
	D=M // 52
	@R13 // 53
	A=M // 54
	M=D // 55
// C_PUSH argument 0
	@0 // 56
	D=A // 57
	@ARG // 58
	A=M+D // 59
	D=M // 60
	@SP // 61
	A=M // 62
	M=D // 63
	@SP // 64
	M=M+1 // 65
// C_PUSH constant 2
	@2 // 66
	D=A // 67
	@SP // 68
	A=M // 69
	M=D // 70
	@SP // 71
	M=M+1 // 72
// sub
	@SP // 73
	M=M-1 // 74
	@SP // 75
	A=M // 76
	D=M // 77
	@SP // 78
	M=M-1 // 79
	@SP // 80
	A=M // 81
	M=M-D // 82
	@SP // 83
	M=M+1 // 84
// C_POP argument 0
	@0 // 85
	D=A // 86
	@ARG // 87
	D=M+D // 88
	@R13 // 89
	M=D // 90
	@SP // 91
	M=M-1 // 92
	A=M // 93
	D=M // 94
	@R13 // 95
	A=M // 96
	M=D // 97
(FibonacciSeries.MAIN_LOOP_START)
// C_PUSH argument 0
	@0 // 98
	D=A // 99
	@ARG // 100
	A=M+D // 101
	D=M // 102
	@SP // 103
	A=M // 104
	M=D // 105
	@SP // 106
	M=M+1 // 107
// goto-if COMPUTE_ELEMENT
	@SP // 108
	M=M-1 // 109
	A=M // 110
	D=M // 111
	@FibonacciSeries.COMPUTE_ELEMENT // 112
	D;JNE // 113
// goto END_PROGRAM
	@FibonacciSeries.END_PROGRAM // 114
	0;JMP // 115
(FibonacciSeries.COMPUTE_ELEMENT)
// C_PUSH that 0
	@0 // 116
	D=A // 117
	@THAT // 118
	A=M+D // 119
	D=M // 120
	@SP // 121
	A=M // 122
	M=D // 123
	@SP // 124
	M=M+1 // 125
// C_PUSH that 1
	@1 // 126
	D=A // 127
	@THAT // 128
	A=M+D // 129
	D=M // 130
	@SP // 131
	A=M // 132
	M=D // 133
	@SP // 134
	M=M+1 // 135
// add
	@SP // 136
	M=M-1 // 137
	@SP // 138
	A=M // 139
	D=M // 140
	@SP // 141
	M=M-1 // 142
	@SP // 143
	A=M // 144
	M=M+D // 145
	@SP // 146
	M=M+1 // 147
// C_POP that 2
	@2 // 148
	D=A // 149
	@THAT // 150
	D=M+D // 151
	@R13 // 152
	M=D // 153
	@SP // 154
	M=M-1 // 155
	A=M // 156
	D=M // 157
	@R13 // 158
	A=M // 159
	M=D // 160
// C_PUSH pointer 1
	@THAT // 161
	D=M // 162
	@SP // 163
	A=M // 164
	M=D // 165
	@SP // 166
	M=M+1 // 167
// C_PUSH constant 1
	@1 // 168
	D=A // 169
	@SP // 170
	A=M // 171
	M=D // 172
	@SP // 173
	M=M+1 // 174
// add
	@SP // 175
	M=M-1 // 176
	@SP // 177
	A=M // 178
	D=M // 179
	@SP // 180
	M=M-1 // 181
	@SP // 182
	A=M // 183
	M=M+D // 184
	@SP // 185
	M=M+1 // 186
// C_POP pointer 1
	@SP // 187
	M=M-1 // 188
	A=M // 189
	D=M // 190
	@THAT // 191
	M=D // 192
// C_PUSH argument 0
	@0 // 193
	D=A // 194
	@ARG // 195
	A=M+D // 196
	D=M // 197
	@SP // 198
	A=M // 199
	M=D // 200
	@SP // 201
	M=M+1 // 202
// C_PUSH constant 1
	@1 // 203
	D=A // 204
	@SP // 205
	A=M // 206
	M=D // 207
	@SP // 208
	M=M+1 // 209
// sub
	@SP // 210
	M=M-1 // 211
	@SP // 212
	A=M // 213
	D=M // 214
	@SP // 215
	M=M-1 // 216
	@SP // 217
	A=M // 218
	M=M-D // 219
	@SP // 220
	M=M+1 // 221
// C_POP argument 0
	@0 // 222
	D=A // 223
	@ARG // 224
	D=M+D // 225
	@R13 // 226
	M=D // 227
	@SP // 228
	M=M-1 // 229
	A=M // 230
	D=M // 231
	@R13 // 232
	A=M // 233
	M=D // 234
// goto MAIN_LOOP_START
	@FibonacciSeries.MAIN_LOOP_START // 235
	0;JMP // 236
(FibonacciSeries.END_PROGRAM)