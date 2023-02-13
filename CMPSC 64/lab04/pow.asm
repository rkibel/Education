# pow.asm program

# Assembly (NON-RECURSIVE) code version of pow(x,n):
.data
    number_prompt: .asciiz "Enter a number x:\n"
    exponent_prompt: .asciiz "Enter the exponent n:\n"
    answer: .asciiz "Power(x,n) is:\n" 
    newline: .asciiz "\n"

#Text Area (i.e. instructions)
.text
main:
	li $v0 4
    la $a0 number_prompt
    syscall

    li $v0 5
    syscall
    move $t0 $v0 #number

    li $v0 4
    la $a0 exponent_prompt
    syscall

    li $v0 5
    syscall
    move $t1 $v0 #exponent

    li $t2 1 #place to store power raised to exponent
    li $t3 0
    jal while_loop

    li $v0 4
    la $a0 answer
    syscall

    li $v0 1
    move $a0 $t2
    syscall

    li $v0 4
    la $a0 newline
    syscall

    j exit

while_loop:
    blt $t3 $t1 multiply
    jr $ra

multiply:
    mult $t2 $t0
    mflo $t2
    addiu $t3 1
    j while_loop

exit:
    li $v0 10
    syscall
