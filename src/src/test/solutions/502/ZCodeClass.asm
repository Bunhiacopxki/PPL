
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

foo:
    addi $sp, $sp, -4
    sw $ra, 0($sp)
	l.s $f0, _
	l.s $f1, __
	add.s $f0, $f0, $f1
	mov.s $f12, $f0
	jal writeNumber
    lw $ra, 0($sp)
    addi $sp, $sp, 4
	jr $ra
main:
    addi $sp, $sp, -4
    sw $ra, 0($sp)
	jal foo
    lw $ra, 0($sp)
    addi $sp, $sp, 4
	jal exit

	.data
_: .float 1.0

	.data
__: .float 1.0
