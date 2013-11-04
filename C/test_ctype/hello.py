from ctypes import cdll, c_char, c_int, c_float,Structure,CFUNCTYPE,POINTER, c_char_p,CDLL

class helloStruct (Structure):
    pass

helloStruct._fields_ = [
    ('i',c_int),
    ('f',c_float)   ]

def callback():
    print ("callback()")
    hs = helloStruct()
    hs.i = 10
    hs.f = 25.5
    return hs


#libc =cdll.msvcrt
libc = CDLL("hello.dll")
helloLib = cdll.hello

helloLib.fxn.restype = helloStruct

TMP_FCN = CFUNCTYPE(POINTER(c_char))

callback_fcn = TMP_FCN(callback)
result = helloLib.fxn(callback_fcn)

print ("result: ",result)
