	.file	"hello.c"
	.section	.rodata
.LC0:
	.string	"i: %d\n"
.LC1:
	.string	"f: %f\n"
	.text
	.globl	fxn
	.type	fxn, @function
fxn:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$64, %rsp
	movq	%rdi, -24(%rbp)
	movq	-24(%rbp), %rdx
	movl	$0, %eax
	call	*%rdx
	movq	%rax, %rcx
	movq	%rdx, %rax
	movq	%rcx, -48(%rbp)
	movq	%rax, -40(%rbp)
	movq	-48(%rbp), %rax
	movq	%rax, -16(%rbp)
	movq	-40(%rbp), %rax
	movq	%rax, -8(%rbp)
	movl	-16(%rbp), %eax
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	movss	-12(%rbp), %xmm0
	unpcklps	%xmm0, %xmm0
	cvtps2pd	%xmm0, %xmm0
	movl	$.LC1, %edi
	movl	$1, %eax
	call	printf
	movss	-12(%rbp), %xmm1
	movl	-16(%rbp), %eax
	cvtsi2ss	%eax, %xmm0
	mulss	%xmm1, %xmm0
	movss	%xmm0, -52(%rbp)
	movl	-52(%rbp), %eax
	movl	%eax, -52(%rbp)
	movss	-52(%rbp), %xmm0
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	fxn, .-fxn
	.ident	"GCC: (Ubuntu/Linaro 4.7.3-1ubuntu1) 4.7.3"
	.section	.note.GNU-stack,"",@progbits
