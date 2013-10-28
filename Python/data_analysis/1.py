import json
from collections import defaultdict

from collections import Counter

from pandas import DataFrame, Series
import pandas as pd

def get_counts(sequence):
    counts = dict()
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts



def get_counts1(sequence):
    counts = defaultdict(int) #initializes values to 0
    #If there are a million records avoiding that if-else can have an noticeable effect in running time.

    for x in sequence:
        counts[x] += 1
    return counts


def get_counts3(sequence):
    counts = Counter(sequence)
    return counts

def top_counts(count_dict,n=10):
    value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-10:]

path = 'pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path)]

print records[0]

timezones = [rec['tz'] for rec in records if 'tz' in rec ]

print "No. of Timezones(with duplicates)"
print len(timezones)

print "No. of Timezones(without duplicates)"
print len(set(timezones))

counts = get_counts(timezones)
counts1 = get_counts1(timezones)


print counts,counts1

print top_counts(timezones)

cnt = get_counts3(timezones)

print dir(cnt),cnt.most_common(10)





