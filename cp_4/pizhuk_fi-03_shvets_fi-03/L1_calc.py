from itertools import product
from sequence import known_sequence
from multiprocessing import Pool
from array import array
from base import LFSR

L1_polynom = [3, 0]


def calc_L1(init):
    L1 = LFSR(init, L1_polynom)
    result = array('B')
    append = result.append
    nxt = L1.next
    for i in range(222):
        append(nxt())
    R = 0
    for i in range(len(result)):
        R += result[i] ^ known_sequence[i]
    if R <= 71:
        return (init, R)


if __name__ == '__main__':
    gen = (array('B', vector) for vector in product([0, 1], repeat=25))
    pool = Pool()
    results = pool.map(calc_L1, gen)
    results = [result for result in results if result]
    print(results)

# beta = 1 / (2 ** 25)
# print(norm.ppf(1 - beta, loc=0, scale=1))
# print(norm.ppf(0.99, loc=0, scale=1))
# C = 70
# N = 222
