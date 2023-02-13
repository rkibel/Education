# min.asm program

.data

        # TODO: Complete these declarations / initializations

        prompt: .asciiz "Enter the next number:\n"
        min: .asciiz "Minimum: "
        newline: .asciiz "\n"

#Text Area (i.e. instructions)
.text
main:
    li $v0 4
    la $a0 prompt
    syscall

    li $v0 5
    syscall
    move $t0 $v0

    li $v0 4
    la $a0 prompt
    syscall

    li $v0 5
    syscall
    move $t1 $v0

    li $v0 4
    la $a0 prompt
    syscall

    li $v0 5
    syscall
    move $t2 $v0

    j exit



exit:
    li $v0 10
    syscall
