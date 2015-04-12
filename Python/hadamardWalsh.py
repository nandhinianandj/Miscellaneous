#  http://www.quantatrisk.com/2015/04/07/walsh-hadamard-transform-python-tests-for-randomness-of-financial-return-series/
def Hadamard2Walsh(n):
    import numpy as np
    from scipy.linalg import hadamard
    from math import log
    hadamardMatrix = hadamard(n)
    HadIdx = np.arange(n)
    M = log(n,2) + 1
    for i in HadIdx:
        s = format(i, '#032b')
        s = s[::-1];
        s = s[:-2];
        s = list(s)
        x = [int(x) for x in s]
        x = np.array(x)
        if(i==0):
            binHadIdx = x
        else:
            binHadIdx = np.vstack((binHadIdx, x))
    binSeqIdx = np.zeros((n,M)).T

    for k in reversed(xrange(1, int(M))):
        tmp = np.bitwise_xor(binHadIdx.T[k], binHadIdx.T[k-1])
        binSeqIdx[k] = tmp
    tmp = np.power(2, np.arange(M)[::-1])
    tmp = tmp.T
    SeqIdx = np.dot(binSeqIdx.T, tmp)

    j = 1
    for i in SeqIdx:
        if(j == 1):
            walshMatrix = hadamardMatrix[i]
        else:
            walshMatrix = np.vstack(walshMatrix, hadamardMatrix[i])
        j+= 1
    return (hadamardMatrix, walshMatrix)
    pass
