
################################################################
#   UniVariate Outliers
##################################################################

def get_outliers(data, m = 2.):
    """
    data -- is a pandas data frame
    """
    # by median
    d = np.abs(data - np.median(data))
    mdev = np.median(d)
    s = d/mdev if mdev else 0.
    return data[s>m]

def 3sigmaDeviation(seq, threshold=3, passes=1):
    # filter and remove values beyond +/- 3 sigma variance
    # default one pass.
    pass

def interQuartileRangeDev(seq, threshold=1.5):
    # filter values beyound the +/- 1.5 quartile range
    pass

def capPercentile(seq, threshold=5):
    # filter values from the 5th and 95th percentile range
    pass


################################################################
#   Multi/Bi-Variate Outliers
##################################################################
#   -- Measured using an index of influence or leverage or distance
#   -- Popular indices such as Mahalanobis’ distance and Cook’s D are frequently used .
#   --  statistical measure like STUDENT, COOKD, RSTUDENT and others.

###
# Removal methods
#    -- Deleting
#    -- Transforming(like log or others) and binning
#    -- Imputing values

