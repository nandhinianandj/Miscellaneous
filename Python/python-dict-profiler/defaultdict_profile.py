import default_dict
import cProfile
import sys
import rpy2

size = [10**i for i in range(4)]
big_dict = {}
keys = xrange(size[0])
for key in keys:
    big_dict.update({key:str(key)})

def defaultdict_try_test():
    a = default_dict.defaultdict_try(big_dict,'try')
    print a['No']

def defaultdict_in_test():
    a = default_dict.defaultdict_in(big_dict,'in')
    print a['None']
    
def main():
    Prof = cProfile.Profile()
    Prof.runcall(defaultdict_try_test)
    Prof.runcall(defaultdict_in_test)
    filed = "prof_stats"
    print Prof.getstats()
    Prof.dump_stats(filed)
    #Prof.print_stats()

if __name__ == '__main__':
    main()
