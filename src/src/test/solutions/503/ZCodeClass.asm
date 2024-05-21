
    .globl writeNumber
    .globl exit
    .globl main
    .text

j main

readNumber:
    li $v0, 5
    syscall
    jr $ra

writeNumber:
    li $v0, 1
    syscall
    jr $ra

exit:
    li $v0, 10
    syscall

main:
    addi $sp, $sp, -4
    sw $ra, 0($sp)
	jal readNumber
	move $t0, $v0
	move $a0, $t0
	jal writeNumber
    lw $ra, 0($sp)
    addi $sp, $sp, 4
	jal exit