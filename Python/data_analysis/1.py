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

#print counts,counts1

print top_counts(counts)

cnt = get_counts3(timezones)

print cnt.most_common(10)

frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
clean_tz_counts = clean_tz.value_counts()

clean_plt = clean_tz_counts[:10].plot(kind='barh',rot=0)
results = Series([x.split()[0] for x in frame.a.dropna()])

cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
by_tz_os = cframe.groupby(['tz',operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()

count_subset = agg_counts.take(indexer)[-10:]
count_subset.plot(kind='barh',stacked=True)

normed_subset = count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table('m1-1m/users.dat',sep='::',header=None,
                      names=unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_table('m1-1m/ratings.dat',sep='::',header=None,
                        names = rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_table('m1-1m/movies.dat',sep='::',header=None,
                       names=mnames)

data = pd.merge(pd.merge(ratings,users),movies)
print data.ix[0]

mean_ratings = data.pivot.table('rating',rows='title',
                                cols='gender',aggfunc='mean')
ratings_by_title = data.groupby('title').size()

active_titles = ratings_by_title.index[ratings_by_title >= 250]

mean_ratings = mean_ratings.ix[active_titles]

top_female_ratings = mean_ratings.sort_index(by='F',ascending=False)

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_index(by='diff')

rating_std_by_title = data.groupby('title')['rating'].std()

rating_std_by_title_active = rating_std_by_title.ix[active_titles]

names1880 = pd.read_csv('names/yob1880.txt',names=['name','sex','births'])
names1880.groupby('sex').births.sum()

year = range(1880,2011)
pieces = []
columns = ['name','sex','births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path,names=columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces,ignore_index=True)
total_births = names.pivot_table('births',rows='year',
                                 cols='sex',aggfunc=sum)

total_births.plot(title='Total births by sex and year')

def add_prop(group):
    births = group.births.astype(float)
    group['prop'] = births/births.sum()
    return group

names = names.groupby(['year','sex']).apply(add_prop)
np.allclose(names.groupby(['year','sex']).prop.sum(),1)

def get_top1000(group):
    return group.sort_index(by='births',ascending=False)[:1000]

grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)

pieces = []
for year,group in names.groupby(['year','sex']):
    pieces.append(group.sort_index(by='births',ascending=False)[:1000])

top1000 = pd.concat(pieces,ignore_index=True)










