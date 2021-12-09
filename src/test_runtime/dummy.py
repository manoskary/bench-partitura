import numpy as np
import timeit
import random
import matplotlib.pyplot as plt

## searches for an item in a list
def contains(lst, x):
    for y in lst:
        if x == y: return True
    return False
ns = np.linspace(10, 10_000, 100, dtype=int)
# red plots
ts = [timeit.timeit('contains(lst, 0)',
                    setup='lst=list(range({})); random.shuffle(lst)'.format(n),
                    globals=globals(),
                    number=100)
      for n in ns]
plt.plot(ns, ts, 'or')
# line of best fit for red plots
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-r')
# blue plots
ts = [timeit.timeit('contains(lst, -1)',
                    setup='lst=list(range({}))'.format(n),
                    globals=globals(),
                    number=100)
      for n in ns]
plt.plot(ns, ts, 'ob')
# line of best fit for blue plots
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')

plt.show()