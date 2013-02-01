def fitness(source,target):
    fitval = 0
    for i in range(0,len(source)):
        fitval += (ord(target[i]) - ord(source[i])) ** 2
    return (fitval)


def mutate(source):
    charpos = random.randint(0,len(source) - 1)
    parts = list(source)
    parts[charpos] = chr(ord(parts[charpos]) + random.randint(-1,1))
    return(''.join(parts))

def crossover(parent1,parent2):
    child_dna = parent1['dna'][:]

    #Mix the dna aka crossover
    start = random.randint(0,len(parent2['dna']) -1)
    stop = random.randit(0,len(parent2['dna']) -1)
    if start > stop:
        stop, start = start,stop
    child_dna[start:stop] = parent2['dna'][start:stop]

    child_fitness = calc_fitness(child_dna,target)
    #Mutate one position
    return ({'dna':mutate(child_dna),'fitness':child_fitness})

def random_parent(genepool):
    wRndNr = random.random()* random.random() * (GENSIZE -1)
    wRndNr = int(wRndNr)
    return genepool[wRndNr]

def main():
    GENSIZE = 20
    genepool = []

    for i in range(0,GENSIZE):
        dna = [random.choice(string.printable[:-5] for j in range(0,len(targeta)))]
        fitness = calc_fitness(dna,target)
        candidate = {'dna':dna,'fitness':fitness}
        genepool.append(candidate)

def main1():

    fitval = fitness(source,target)
    i = 0
    while True:
        i += 1
        m = mutate(source)
        fitval_m = fitness(m,target)
        source = m
        print "%5i %5i %14s" %(i, fitval_m,m)
        if fitval == 0:
            break

def main2():
    while True:
        genepool.sort(key=lambda candidate: candidate['fitness'])
        if genepool[0]['fitness'] == 0:
            # Target reached
            break
        parent1 = random_parent(genepool)
        parent2 = random_parent(genepool)

        child = mutate(parent1,parent2)
        if child['fitness'] < genepool[-1]['fitness']:
            genepool[-1] = child
