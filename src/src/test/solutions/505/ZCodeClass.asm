
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
    la $t2, c
	la $t0, a
	la $t1, b
    jal concat
    la $t2, f
	la $t0, d
	la $t1, e
    jal concat
	la $a0, c
	jal writeString
	la $a0, f
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
b: .asciiz "cde"

	.data
____STRING: .space 100

	.data
c: .space 100

	.data
______STRING: .asciiz "1"

	.data
d: .asciiz "1"

	.data
________STRING: .asciiz "2"

	.data
e: .asciiz "2"

	.data
__________STRING: .space 100

	.data
f: .space 100
