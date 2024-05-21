    .globl writeNumber
    .globl exit
    .globl main
    .text

j main

writeNumber:
    li $v0, 1
    syscall
    jr $ra

exit:
    li $v0, 10
    syscall