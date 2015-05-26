import pandas as pd
import numpy as np
from sklearn import tree
from collections import OrderedDict
import json
import mp_generic as mp

bidders =pd.read_csv('bidder.csv')
bids = pd.read_csv('bids.csv')
test = pd.read_csv('test.csv')

auctionWiseBids = dict()
uniqueAuctions = pd.Series(bids.auction).unique()
uniqueBidders = pd.Series(bids.bidder_id).unique()
bidderWiseBidTimes = dict()
tenKBids = bids[:10000]
#for auction in uniqueAuctions:
#    auctionWiseBids[auction] = tenKBids[tenKBids['auction'] == auction]

def accumulateBids(args):
    bidder = str(args.get('bidder_id'))
    for each in bids[bids['bidder_id'] == bidder]['time']:
        if bidderWiseBidTimes.has_key(bidder):
            bidderWiseBidTimes[bidder].append(each)
        else:
            bidderWiseBidTimes[bidder] = [each]

bids.groupby('bidder_id').apply(accumulateBids)
#mp.mp_groupby(bids, 'bidder_id', accumulateBids)

with open('./bidderWiseBidTimes.json') as fd:
    json.dump(bidderWiseBidTimes,fd, ensure_ascii=False)

bidIntervalsAverage = list()
outcomes = list()
# Build parameters to use for decision tree learning
# parameters: bidder average bid times,
for bidder in bidders.iterrows():
    if bidderWiseBidTimes.has_key(bidder[1]['bidder_id']):
        bidIntervalsAverage.append(np.average(bidderWiseBidTimes[bidder[1]['bidder_id']]))
        outcomes.append(bidders['outcome'])

clf = tree.DecisionTreeClassifier()
clf.fit(bidIntervalsAverage, outcomes)


for bid in bids[10000:20000]:
    clf.predict()
