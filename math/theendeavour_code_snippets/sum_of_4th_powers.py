import collections
import math


upper_bound = int(math.ceil(math.sqrt(653518657)))

cnt = collections.Counter(x**4 + y**4 for x in range(1,upper_bound) for y in range(1,upper_bound))# if x>=y)

[x for x in cnt if cnt[x] == 2]


