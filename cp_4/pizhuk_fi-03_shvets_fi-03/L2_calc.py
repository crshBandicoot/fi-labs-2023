from itertools import product

from scipy.stats import norm

from sequence import known_sequence
from multiprocessing import Pool
from array import array
from base import LFSR

L2_polynom = [6, 2, 1, 0]


def calc_L2(init):
    L2 = LFSR(init, L2_polynom)
    result = array('B')
    append = result.append
    nxt = L2.next
    for i in range(229):
        append(nxt())
    R = 0
    for i in range(len(result)):
        R += result[i] ^ known_sequence[i]
    if R <= 73:
        return (init, R)


if __name__ == '__main__':
    gen = (array('B', vector) for vector in product([0, 1], repeat=26))
    pool = Pool()
    results = pool.map(calc_L2, gen)
    results = list(filter(None, results))
    print(results)

# beta = 1 / (2 ** 26)
# print(norm.ppf(1 - beta, loc=0, scale=1))
# print(norm.ppf(0.99, loc=0, scale=1))
# C = 73
# N = 229
