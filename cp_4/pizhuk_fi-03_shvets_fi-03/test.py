from base import LFSR
from array import array

test = LFSR(array('B', [0, 0, 1, 0, 1, 1]), [1, 3])
res = []
for _ in range(50):
    res.append(test.next())
print(''.join([str(el) for el in res]))
