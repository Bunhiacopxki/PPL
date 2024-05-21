
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

concat:
    copy_loop_a:
        lb $t3, 0($t0)
        beqz $t3, copy_loop_b
        sb $t3, 0($t2)
        addi $t0, $t0, 1
        addi $t2, $t2, 1 
        j copy_loop_a
    copy_loop_b:
        lb $t3, 0($t1)
        beqz $t3, end
        sb $t3, 0($t2)
        addi $t1, $t1, 1
        addi $t2, $t2, 1
        j copy_loop_b
    end:
        sb $zero, 0($t2)
        jr $ra

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
    la $t2, __STRING
	la $t1, __STRING
	la $a0, __STRING
	jal writeString
    la $t2, ____STRING
	la $t0, ___STRING
	la $t1, a
    jal concat
	la $a0, ____STRING
	jal writeString
    lw $ra, 0($sp)
    addi $sp, $sp, 4
	jal exit

	.data
STRING: .asciiz "abc"

	.data
a: .asciiz "abc"

	.data
__STRING: .asciiz "cde"

	.data
___STRING: .asciiz "abc"

	.data
____STRING: .space 100
