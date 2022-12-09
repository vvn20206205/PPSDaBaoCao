import numpy as np
import math


def Nhan2MaTran(MaTran1, MaTran2):
    # Tính toán ma trận
    # ([1,m] x [m,n])
    MaTran1 = np.asarray(MaTran1)
    MaTran2 = np.asarray(MaTran2)
    HeSoPt = MaTran1@MaTran2
    return HeSoPt


def Nhan1List_1So(List, a):
    # Tính toán 1 list
    for i in range(len(List)):
        List[i] = List[i]*a
    return List


def TinhTySaiPhan(MaTranA):
    # Tính tỷ sai phân
    # Lấy tỷ hiệu chia cho giai thừa
    MaTran1 = list(MaTranA)
    for i in range(len(MaTranA)):
        MaTran1[i] = MaTranA[i]/math.factorial(i)

    return MaTran1

