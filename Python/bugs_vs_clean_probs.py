# copy paste these into a ipython shell started with ipython --pylab

import numpy as np

p = np.linspace(0,1,50)

plt.plot(p,2*p/(1+p),color='#348ABD',lw=3)

plt.scatter(0.2,2*(0.2)/1.2,s = 140,c = '#348ABD')

plt.xlim(0,1)

plt.ylim(0,1)

plt.xlabel("Prior,$P(A) = p$")

plt.ylabel("Posterior, $P(A|X) $, with $P(A) = p$")

plt.title("Are there bugs in my code??")

