# -*- coding: utf-8 -*-
# -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.#

#* File Name : tpot_regreession_ex.py
#
#* Purpose :
#
#* Creation Date : 25-04-2019
#
#* Last Modified : Thursday 25 April 2019 05:54:41 PM IST
#
#* Created By :

#_._._._._._._._._._._._._._._._._._._._._.#

from tpop import TPOTRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

housing=load_boston()
X_train, X_test,  y_train, y_test = train_test_split(housing.data, housing.target,
                                                        train_size=0.75, test_size=0.25)

tpot=TPOTRegressor(generations=5, population_size=20, verbosity=2)
tpot.fit(X_train, y_train)
print(tpot.score(X_test, y_test))
tpot.export('tpot_boston_regression_pipeline.py')
