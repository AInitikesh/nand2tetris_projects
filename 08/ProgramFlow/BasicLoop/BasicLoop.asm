
// C_PUSH constant 0
	@0 // 0
	D=A // 1
	@SP // 2
	A=M // 3
	M=D // 4
	@SP // 5
	M=M+1 // 6
// C_POP local 0
	@0 // 7
	D=A // 8
	@LCL // 9
	D=M+D // 10
	@R13 // 11
	M=D // 12
	@SP // 13
	M=M-1 // 14
	A=M // 15
	D=M // 16
	@R13 // 17
	A=M // 18
	M=D // 19
($LOOP_START)
// C_PUSH argument 0
	@0 // 20
	D=A // 21
	@ARG // 22
	A=M+D // 23
	D=M // 24
	@SP // 25
	A=M // 26
	M=D // 27
	@SP // 28
	M=M+1 // 29
// C_PUSH local 0
	@0 // 30
	D=A // 31
	@LCL // 32
	A=M+D // 33
	D=M // 34
	@SP // 35
	A=M // 36
	M=D // 37
	@SP // 38
	M=M+1 // 39
// add
	@SP // 40
	M=M-1 // 41
	@SP // 42
	A=M // 43
	D=M // 44
	@SP // 45
	M=M-1 // 46
	@SP // 47
	A=M // 48
	M=M+D // 49
	@SP // 50
	M=M+1 // 51
// C_POP local 0
	@0 // 52
	D=A // 53
	@LCL // 54
	D=M+D // 55
	@R13 // 56
	M=D // 57
	@SP // 58
	M=M-1 // 59
	A=M // 60
	D=M // 61
	@R13 // 62
	A=M // 63
	M=D // 64
// C_PUSH argument 0
	@0 // 65
	D=A // 66
	@ARG // 67
	A=M+D // 68
	D=M // 69
	@SP // 70
	A=M // 71
	M=D // 72
	@SP // 73
	M=M+1 // 74
// C_PUSH constant 1
	@1 // 75
	D=A // 76
	@SP // 77
	A=M // 78
	M=D // 79
	@SP // 80
	M=M+1 // 81
// sub
	@SP // 82
	M=M-1 // 83
	@SP // 84
	A=M // 85
	D=M // 86
	@SP // 87
	M=M-1 // 88
	@SP // 89
	A=M // 90
	M=M-D // 91
	@SP // 92
	M=M+1 // 93
// C_POP argument 0
	@0 // 94
	D=A // 95
	@ARG // 96
	D=M+D // 97
	@R13 // 98
	M=D // 99
	@SP // 100
	M=M-1 // 101
	A=M // 102
	D=M // 103
	@R13 // 104
	A=M // 105
	M=D // 106
// C_PUSH argument 0
	@0 // 107
	D=A // 108
	@ARG // 109
	A=M+D // 110
	D=M // 111
	@SP // 112
	A=M // 113
	M=D // 114
	@SP // 115
	M=M+1 // 116
// goto-if $LOOP_START
	@SP // 117
	M=M-1 // 118
	A=M // 119
	D=M // 120
	@$LOOP_START // 121
	D;JNE // 122
// C_PUSH local 0
	@0 // 123
	D=A // 124
	@LCL // 125
	A=M+D // 126
	D=M // 127
	@SP // 128
	A=M // 129
	M=D // 130
	@SP // 131
	M=M+1 // 132