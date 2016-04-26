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

a = Argument(ptr(const_float_))
b = Argument(ptr(const_float_))
c = Argument(ptr(float_))

with Function("matmul", (a, b, c)) as asm_matmul_function:
    reg_a = GeneralPurposeRegister64()
    LOAD.ARGUMENT(reg_a, a)

    reg_b = GeneralPurposeRegister64()
    LOAD.ARGUMENT(reg_b, b)

    reg_c = GeneralPurposeRegister64()
    LOAD.ARGUMENT(reg_c, c)

    xmm_Brow0 = XMMRegister()
    MOVUPS(xmm_Brow0, [reg_b + 0])

    xmm_Brow1 = XMMRegister()
    MOVUPS(xmm_Brow1, [reg_b + 16])

    xmm_Brow2 = XMMRegister()
    MOVUPS(xmm_Brow2, [reg_b + 32])

    xmm_Brow3 = XMMRegister()
    MOVUPS(xmm_Brow3, [reg_b + 48])

    for k in range(4):
        xmm_Ak0 = XMMRegister()
        MOVSS(xmm_Ak0, [reg_a + k * 16])
        SHUFPS(xmm_Ak0, xmm_Ak0, 0x00)
        MULPS(xmm_Ak0, xmm_Brow0)

        xmm_Ak1 = XMMRegister()
        MOVSS(xmm_Ak1, [reg_a + k * 16 + 4])
        SHUFPS(xmm_Ak1, xmm_Ak1, 0x00)
        MULPS(xmm_Ak1, xmm_Brow1)
        ADDPS(xmm_Ak0, xmm_Ak1)

        xmm_Ak2 = XMMRegister()
        MOVSS(xmm_Ak2, [reg_a + k * 16 + 8])
        SHUFPS(xmm_Ak2, xmm_Ak2, 0x00)
        MULPS(xmm_Ak2, xmm_Brow2)

        xmm_Ak3 = XMMRegister()
        MOVSS(xmm_Ak3, [reg_a + k * 16 + 12])
        SHUFPS(xmm_Ak3, xmm_Ak3, 0x00)
        MULPS(xmm_Ak3, xmm_Brow3)
        ADDPS(xmm_Ak2, xmm_Ak3)

        ADDPS(xmm_Ak0, xmm_Ak2)
        MOVUPS([reg_c + k * 16], xmm_Ak0)

    RETURN()

python_matmul_function = asm_matmul_function.finalize(abi.detect()).encode().load()
print(python_add_function([2,3,5], [2])) # -> prints "4"
