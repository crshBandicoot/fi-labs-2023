from array import array


class LFSR:
    def __init__(self, initial: array, polynom: list[int]):
        self.sequence = initial
        self.polynom = polynom

    def next(self):
        seq = self.sequence
        pol = self.polynom
        result = seq[0]
        nxt = seq[pol[0]] ^ seq[pol[1]]
        for el in pol[2:]:
            nxt = nxt ^ seq[el]
        seq.pop(0)
        seq.append(nxt)
        return result


class Geffe:
    def __init__(self, L1: LFSR, L2: LFSR, L3: LFSR):
        self.L1 = L1
        self.L2 = L2
        self.L3 = L3

    def next(self):
        x = self.L1.next()
        y = self.L2.next()
        s = self.L3.next()
        return (s & x) ^ ((1 ^ s) & y)
