import scipy
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

normal_dist = scipy.stats.norm()
norm_rand_values = scipy.stats.norm.rvs(size=1000)
x = np.linspace(scipy.stats.norm.ppf(0.01),
                scipy.stats.norm.ppf(0.99), 100)

fig, ax = plt.subplots()
ax.plot(x, normal_dist.pdf(x), 'k-',label='pdf')
ax.plot(x, normal_dist.cdf(x), 'r-',label='cdf')
ax.hist(norm_rand_values, density=True, bins='auto', histtype='stepfilled', alpha=0.2)
ax.set_xlim([x[0], x[-1]])
ax.set_xlabel('x')
ax.set_ylabel('f(x), F(x)')
ax.set_title('Testing normal distribution')
plt.legend()
plt.savefig('test_normal_distribution.png',dpi=600)
plt.close()

mu = 0.8
poisson_dist = scipy.stats.poisson(mu)
poisson_rand_values = scipy.stats.poisson.rvs(mu, size=1000)
x = np.arange(10)
fig, ax = plt.subplots()
ax.vlines(x, 0, poisson_dist.cdf(x), colors='r', linestyles='-', lw=2, alpha=0.5,
        label='cdf')
ax.plot(x, poisson_dist.pmf(x), 'ko', ms=8, label='pmf')
ax.hist(poisson_rand_values, density=True, bins='auto', alpha=0.2)

ax.set_xlabel('x')
ax.set_ylabel('f(x), F(x)')
ax.set_title('Testing Poisson distribution')
plt.legend()
plt.savefig('test_poisson_distribution.png',dpi=600)
plt.close()

print(scipy.stats.ttest_ind(norm_rand_values,poisson_rand_values))
