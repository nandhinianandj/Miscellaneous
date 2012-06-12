import scipy as sp
import scipy.stats
import matplotlib.pyplot as plt

def pdf(y,n,k):
    Phi = scipy.stats.norm.cdf(y)
    phi = scipy.stats.norm.pdf(y)
    return scipy.stats.beta.pdf(Phi,k,n+1-k)*phi

def plot_percentile(p):
    center = scipy.stats.norm.ppf(0.01*p)
    t = sp.linspace(center-0.25,center+0.25,100)
    plt.plot(t,pdf(t,1000,10*p))
    plt.title("{0}th percentile".format(p))

plt.subplot(221)
plot_percentile(50)
plt.subplot(222)
plot_percentile(75)
plt.subplot(223)
plot_percentile(90)
plt.subplot(224)
plot_percentile(95)
plt.show()

