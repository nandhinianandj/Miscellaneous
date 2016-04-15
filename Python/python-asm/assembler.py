# These two lines are not needed for PeachPy, but will help you get autocompletion in good code editors
from peachpy import *
from peachpy.x86_64 import *

# Lets write a function float DotProduct(const float* x, const float* y)

# If you want maximum cross-platform compatibility, arguments must have names
x = Argument(ptr(const_float_), name="x")
# If name is not specified, it is auto-detected
y = Argument(ptr(const_float_))

# Everything inside the `with` statement is function body
with Function("DotProduct", (x, y), float_,
  # Enable instructions up to SSE4.2
  # PeachPy will report error if you accidentially use a newer instruction
  target=uarch.default + isa.sse4_2):

  # Request two 64-bit general-purpose registers. No need to specify exact names.
  reg_x, reg_y = GeneralPurposeRegister64(), GeneralPurposeRegister64()

  # This is a cross-platform way to load arguments. PeachPy will map it to something proper later.
  LOAD.ARGUMENT(reg_x, x)
  LOAD.ARGUMENT(reg_y, y)

  # Also request a virtual 128-bit SIMD register...
  xmm_x = XMMRegister()
  # ...and fill it with data
  MOVAPS(xmm_x, [reg_x])
  # It is fine to mix virtual and physical (xmm0-xmm15) registers in the same code
  MOVAPS(xmm2, [reg_y])

  # Execute dot product instruction, put result into xmm_x
  DPPS(xmm_x, xmm2, 0xF1)

  # This is a cross-platform way to return results. PeachPy will take care of ABI specifics.
  RETURN(xmm_x)


