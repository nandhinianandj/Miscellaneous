def mergesort(list1):
    assert isinstance(list1, list)
    if len(list1) <= 2:
        return sort(list1)
    #while len(list1) > 2:
    else:
        ls1, ls2 = list1[:int(len(list1)/2)], list1[int(len(list1)/2):]
        return merge(mergesort(ls1), mergesort(ls2))


def merge(ls1, ls2):
    #TODO: assumpes ls1 and ls2 are sorted internally
    if ls1[-1] < ls2[0]:
        ls1.extend(ls2)
        return ls1
    elif ls2[-1] < ls1[0]:
        ls2.extend(ls1)
        return ls2
    else:
        newList = []
        #Damn now we need to find where the lists overlap and insert
    	while ls1 and ls2:
    	    if ls1[0] < ls2[0]:
    	        newList.append(ls1.pop(0))
    	    else:
    	        newList.append(ls2.pop(0))
    	return newList + ls1 + ls2

def sort(ls):
    assert len(ls) <= 2
    if len(ls) == 1:
        return ls
    if ls[0] > ls[1]:
        ls.reverse()
    return ls

