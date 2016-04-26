import percache
cache = percache.Cache('/tmp/collatz-cache')

@cache
def collatz(n):
  out =[]
  while n!=1:
    if n % 2 == 0:
      n/=2
    else:
      n=3*n +1
    out.append(n)
  return len(out)

for i in range(1000):
    collatz_len = {i: len(collatz(i))}

sorted = sorted(collatz_len.items(),key=operator.itemgetter(1))
print(sorted[0])
