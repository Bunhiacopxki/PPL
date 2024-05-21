
    .globl readNumber
    .globl writeNumber
    .globl writeString
    .globl exit
    .globl main
    .data
_TRUE:  .asciiz "true"
_FALSE: .asciiz "false"
    .text

j main

readNumber:
    li $v0, 5
    syscall
    jr $ra

writeNumber:
    li $v0, 2
    syscall
    jr $ra

writeBool:
	li $v0, 4
    syscall
    jr $ra

writeString:
	li $v0, 4
    syscall
    jr $ra

exit:
    li $v0, 10
    syscall

main:
    addi $sp, $sp, -4
    sw $ra, 0($sp)
	l.s $f0, a
	la $a0, _TRUE
	jal writeBool
    lw $ra, 0($sp)
    addi $sp, $sp, 4
	jal exit

	.data
a: .float 1.0
