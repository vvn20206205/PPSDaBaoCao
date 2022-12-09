from math import factorial
# Phương pháp Hoocne


def NhanXTruC(HeSoThuong_Bn: list, c: float):
    # Chức năng: Nhân đa thức (HeSoThuong_Bn) với (x - c)
    HeSoTich_An = list(HeSoThuong_Bn)
    HeSoTich_An.append(0)
    for i in range(1, len(HeSoTich_An)):
        HeSoTich_An[i] -= HeSoThuong_Bn[i-1]*c
    return HeSoTich_An


def ChiaXTruC(HeSoTich_An: list, c: float):
    # Chức năng: Chia đa thức (HeSoThuong_Bn) với (x - c)

    HeSoThuong_Bn = list(HeSoTich_An)
    for i in range(1, len(HeSoTich_An)):
        HeSoThuong_Bn[i] += HeSoThuong_Bn[i-1]*c
    SoDuR = HeSoThuong_Bn.pop(-1)
    return HeSoThuong_Bn, SoDuR


def TinhGiaTri(HeSoDaThuc: list, c: float):
    # Chức năng: Tính giá trị đa thức với (x = c)

    HeSoThuong_Bn = list(HeSoDaThuc)
    for i in range(1, len(HeSoDaThuc)):
        HeSoThuong_Bn[i] += HeSoThuong_Bn[i-1]*c
    return HeSoThuong_Bn[-1]


def DaoHam1(HeSoDaThuc: list, c: float):
    # Chức năng: Tính đạo hàm cấp 1
    HeSoQx, SoDuR = ChiaXTruC(HeSoDaThuc, c)
    return TinhGiaTri(HeSoQx, c)


def DaoHamCapCao(HeSoDaThuc: list, c: float):
    # Chức năng: Tính đạo hàm các cấp
    SoLanLap = len(HeSoDaThuc)-1
    HeSoDaoHam = []
    Bn, R = ChiaXTruC(HeSoDaThuc, c)

    for i in range(1, SoLanLap):
        Bn, R = ChiaXTruC(Bn, c)
        HeSoDaoHam.append(R*i)
        if (i == SoLanLap-1):
            HeSoDaoHam.append(Bn[0]*factorial(i+1))

    return HeSoDaoHam


def W_n_x(list_x: list):
    HeSoTich = [1, -list_x[0]]
    for i in range(1, len(list_x)):
        HeSoTich = NhanXTruC(HeSoTich, list_x[i])
    return HeSoTich

