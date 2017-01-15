import operator

def complement_operator(op):
    if op == operator.add:
        return operator.sub
    elif op == operator.sub:
        return operator.add
    else:
        raise "Only addition/subtraction supported for now"

def unity(op):
    if op in [operator.add, operator.sub]:
        return 1
    raise "Only addition/subtraction supported for now"

def min_gt_1(lst):
    """
    Return minimum value that is > 1
    Works because in this context lst is always sorted in descending order
    """
    for each in lst[::-1]:
        if each == 1:
            continue
        else:
            return each
    return None

def generate(n, typ='int', op=None, empty=False):
    result = set()
    assert typ in ['int', 'set']
    if typ=='int':
        assert op
        #TODO:
        final_op = complement_operator(op)

        result.add(tuple([n]))
        #first = sorted([int(n/2), n-int(n/2)], reverse=True)
        first = [n-1,1]
        result.add(tuple(first))
        prev=first
        mval = min_gt_1(prev)
        import pdb; pdb.set_trace()
        while mval:
            print(mval,prev)
            split_idx = len(prev) - 1 - prev[::-1].index(mval)
            nxt = prev[:split_idx]
            nxt.append(mval-1)
            nxt.extend([1]*(n-sum(nxt)))
            result.add(tuple(nxt))
            mval = min_gt_1(nxt)
            prev=nxt
        return result
    else:

        if empty:
            result.add(tuple(lst))
        pass
    pass

if __name__ == '__main__':
    import sys

    assert sys.argv
    #n = sys.argv[0]
    n = 7
    ans = generate(n, typ='int', op=operator.add)
    print(ans)
    print(len(ans))
