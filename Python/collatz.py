import math
def is_pow_of_2(num):
    """
    @return: returns power value if not returns False
    """
    return num != 0 and ((num & (num - 1)) == 0)
    # import math
    # res = math.log(n, 2)
    # if (res - int(res)) == 0:
    #    return res
    #else:
    #    return false

class Collatz:
    def __init__(self, n):
        self.num = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.num % 2 == 0:
            self.num = self.num/2
            return self.num
        elif self.num == 1:
            raise StopIteration
        else:
            self.num = 3 * self.num + 1
            return self.num

def main(n):
    import pdb; pdb.set_trace()  # XXX BREAKPOINT
    collatz_length = dict()
    length = 0
    c = Collatz(n)
    for x in c:
        if x in collatz_length.keys():
            length += collatz_length[x]
            break
        elif is_pow_of_2(int(x)):
            collatz_length[x] = math.log(x, 2)
            length += collatz_length[x]
            break
        else:
            length += 1
        #print(str(x) + "\t" + str(length))
        #print()
    collatz_length[n] = length
    print(collatz_length)

if __name__ == '__main__':
    #import cProfile
    #cProfile.run('main()')
    import sys
    #for i in range(int(sys.argv[1])):#1000000):
    #    main(i)
    main(int(sys.argv[1]))
