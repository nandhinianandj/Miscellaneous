# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : lincolns_no_errors.py
#
#* Purpose :
#
#* Creation Date : 20-11-2018
#
#* Last Modified : Tue 20 Nov 2018 08:53:11 AM IST
#
#* Created By : John D cook
# Copied from https://www.johndcook.com/blog/2010/07/13/lincoln-index/?utm_content=buffer6cc86&utm_medium=social&utm_source=twitter.com

#_._._._._._._._._._._._._._._._._._._._._.#

from random import random

def find_error(p):
    "Find an error with probability p"
    if random() < p:
        return 1
    return 0

def simulate(true_error_count, p1, p2, reps=10000):
    """Simulate Lincoln's method for estimating errors
    given the true number of errors, each person's probability
    of finding an error, and the number of simulations to run."""
    estimation_error_sum = 0
    for rep in xrange(reps):
        caught1 = 0
        caught2 = 0
        caught_both = 0
        for error in xrange(true_error_count):
            found1 = find_error(p1)
            found2 = find_error(p2)
            caught1 += found1
            caught2 += found2
            caught_both += found1*found2

    estimate = caught1*caught2 / float(caught_both)
    estimation_error_sum += abs(estimate - true_error_count)
    return estimation_error_sum / float(reps)
