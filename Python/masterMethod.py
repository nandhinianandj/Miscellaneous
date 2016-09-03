import operator

def masterMethod(lst, cmp=operator.gt, mergeFunc=None):
    length = int(len(lst))
    if length > 1:
        lst1, lst2 = lst[:int(length/2)], lst[int(length/2):]
        masterMethod(lst1, cmp=cmp)
        masterMethod(lst2, cmp=cmp)

        i=0
        j=0
        k=0

        while i < len(lst1) and j < len(lst2):
            if cmp(lst1[i], lst2[j]):
                lst[k]=lst1[i]
                i=i+1
            else:
                lst[k]=lst2[j]
                j=j+1
            k=k+1

        while i < len(lst1):
            lst[k]=lst1[i]
            i=i+1
            k=k+1

        while j < len(lst2):
            lst[k]=lst2[j]
            j=j+1
            k=k+1
    return lst
    pass

alist = [54,26,93,17,77,31,44,55,20]
print(alist)
print(masterMethod(alist))
print(masterMethod(alist,cmp=operator.lt))

