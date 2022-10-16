.data

.text

main:
	li $t0, 57 
	li $t1, 32 
	li $t2, 174
	
	addu $t3, $t2, $t1
	sub $t3, $t3, $t0
	sub $t4, $t2, $t1
	xor $t3, $t3, $t4	

	li $v0, 1
	move $a0, $t3
	syscall
	
	j exit

exit:
	li $v0, 10
	syscall

