from L2_results import results as l2_results
from L1_results import results as l1_results
from base import LFSR, Geffe

L1_polynom = [3, 0]
L2_polynom = [6, 2, 1, 0]
L3_polynom = [5, 2, 1, 0]


def calc_L3(init):
    L3 = init
    for l1_input in l1_results:
        L1 = LFSR(l1_input, L1_polynom)
        for l2_input in l2_results:
            L2 = LFSR(l2_input, L2_polynom)
            geffe = Geffe
