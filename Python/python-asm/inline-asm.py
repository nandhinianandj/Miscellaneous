from peachpy import *
from peachpy.x86_64 import *

x = Argument(int32_t)
y = Argument(int32_t)

with Function("Add", (x, y), int32_t) as asm_add_function:
    reg_x = GeneralPurposeRegister32()
    reg_y = GeneralPurposeRegister32()

    LOAD.ARGUMENT(reg_x, x)
    LOAD.ARGUMENT(reg_y, y)

    ADD(reg_x, reg_y)

    RETURN(reg_x)

python_add_function = asm_add_function.finalize(abi.detect()).encode().load()

print(python_add_function(2, 2)) # -> prints "4"

with Function("Fib", (x), int32_t) as asm_fib_function:
    reg_x = GeneralPurposeRegister32()
    reg_xmm = XMMRegister()

_fib:
    pushl %ebp
    MOVUPS(reg_xmm, reg_x)
    movl  %esp, %ebp
    pushl %ebx
    pushl %ecx
    # Saved Registers

    movl 8(%ebp), %ecx          # ecx = n
    movl $0, %ebx               # ebx = secondlast = 1
    movl $1, %eax               # eax = last = 0
    jmp    fib2
fib1:
    add  %ebx, %eax             # last = last + secondlast
    neg  %ebx
    add  %eax, %ebx             # secondlast = –secondlast + last
    dec  %ecx                   # n = n – 1
fib2:
    cmp  $0, %ecx
    jne  fib1                   # if n != 0 goto fib1

    # Restore registers and return
    popl %ecx
    popl %ebx
    popl %ebp
    ret
