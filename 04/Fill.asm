// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.


    @KBD
    D=A

    @end
    M=D

    @status
    M=0

(KBDKEY)

    @KBD
    D=!M

    @status
    D=D&M
    D=D+1

    @SCREENOFF
    D;JEQ

    @status
    D=!M

    @KBD
    D=D&M

    @SCREENON
    D;JNE

    @KBDKEY
    0;JMP

(SCREENON)
    @SCREEN
    D=A
    @i
    M=D
(LOOP1)

    @i
    A=M
    M=-1

    @i
    M=M+1

    @end
    D=M

    @i
    D=D-M    

    @LOOP1
    D;JGT

    @status
    M=-1

    @KBDKEY
    0;JMP

(SCREENOFF)
    @SCREEN
    D=A
    @i
    M=D
(LOOP2)

    @i
    A=M
    M=0

    @i
    M=M+1

    @end
    D=M

    @i
    D=D-M    

    @LOOP2
    D;JGT

    @status
    M=0

    @KBDKEY
    0;JMP



    

