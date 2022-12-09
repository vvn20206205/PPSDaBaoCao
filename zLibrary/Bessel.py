import CONST
import numpy as np
import Hoocne


def ChonTrungTam(MangX, DiemCanTinhGiaTri, GiaTriDiemTT0, GiaTriDiemTT1):
    # Thuật toán
    iChon = 0
    if ((GiaTriDiemTT0 == 0) and (GiaTriDiemTT1 == 0)):
        min = DiemCanTinhGiaTri
        for i in range(len(MangX)):
            if (min > abs(MangX[i]-DiemCanTinhGiaTri)):
                min = abs(MangX[i]-DiemCanTinhGiaTri)
                iChon = i
    else:
        # khác 0: Mốc nội suy trung tâm từ file input
        for i in range(len(MangX)):
            if (abs(MangX[i]-GiaTriDiemTT0) < CONST.EPSILON):
                iChon = i
                break
    # Xác định x0
    if ((MangX[iChon] < DiemCanTinhGiaTri) and (DiemCanTinhGiaTri < MangX[iChon+1])):
        iChon += 0
    else:
        iChon -= 1
   # Thuật toán

    # OUTPUT_STRING
    if (True):
        OUT_String = """
            <h4>- Gói 0: Chọn index mốc nội suy trung tâm</h4>
        """
        if ((GiaTriDiemTT0 == 0) and (GiaTriDiemTT1 == 0)):
            OUT_String += f"""
                \tCHỌN KHOẢNG NỘI SUY TRUNG TÂM PHÙ HỢP VỚI ĐIỂM CẦN TÍNH GIÁ TRỊ:
                <b class="red">(X NGANG = {DiemCanTinhGiaTri})</b>
            """
        else:
            OUT_String += f"""
                \tKHOẢNG NỘI SUY TRUNG TÂM ĐÃ CHỌN TRONG FILE:
                <b class="red">(X0 = {(GiaTriDiemTT0)})</b>
                -->
                <b class="red">(X1 = {(GiaTriDiemTT1)})</b>
            """
        GiaTriDiemTT0 = MangX[iChon]
        GiaTriDiemTT1 = MangX[iChon+1]
        OUT_String += f"""
                \n<br>
                \n=> KHOẢNG NỘI SUY TRUNG TÂM: <b class="blue">({GiaTriDiemTT0};{GiaTriDiemTT1})</b>
            """
    # OUTPUT_STRING

    return iChon, OUT_String


def ToiUuMoc(MangX, MangY, iChonTT):
    print("✅Chọn các mốc phù hợp với PP")
    if (iChonTT == len(MangX)-iChonTT-2):
        print("✅Không cần tối ưu mốc")
        return MangX, MangY

    if (iChonTT < len(MangX)-iChonTT-1):
        print("✅Bên trái có ít hơn")
        MangX = (MangX[:(2*iChonTT+2)])
        MangY = (MangY[:(2*iChonTT+2)])
        return MangX, MangY

    if (iChonTT > len(MangX)-iChonTT-1):
        print("✅Bên phải có ít hơn")
        MangX = (MangX[(iChonTT - (len(MangX)-iChonTT-2)):])
        MangY = (MangY[(iChonTT - (len(MangY)-iChonTT-2)):])
        return MangX, MangY


def TyHieuGauss1X0(MangY):
    iChonTT = len(MangY)//2-1

    Mang1 = [MangY[iChonTT]]
    Mang2 = [MangY[iChonTT]]
    MangTong = [MangY[iChonTT]]

    dem = 0
    for i in range(len(MangY)-1):
        if (i % 2 == 0):
            dem += 1
            GiaTri = MangY[iChonTT+dem]
            for j in range(len(Mang2)):
                GiaTri -= Mang2[j]
                Mang2[j] += GiaTri
            Mang1.append(GiaTri)
            Mang2.append(GiaTri)
        else:
            GiaTri = (MangY[iChonTT-dem])
            for j in range(len(Mang1)):
                GiaTri = Mang1[j]-GiaTri
                Mang1[j] -= GiaTri
            Mang1.append(GiaTri)
            Mang2.append(GiaTri)

        MangTong.append(Mang1[-1])
    return MangTong


def TyHieuGauss2X1(MangY):
    iChonTT = len(MangY)//2

    Mang1 = [MangY[iChonTT]]
    Mang2 = [MangY[iChonTT]]
    MangTong = [MangY[iChonTT]]

    dem = 0
    for i in range(len(MangY)-1):
        if (i % 2 == 1):
            GiaTri = MangY[iChonTT+dem]
            for j in range(len(Mang2)):
                GiaTri -= Mang2[j]
                Mang2[j] += GiaTri
            Mang1.append(GiaTri)
            Mang2.append(GiaTri)
        else:
            dem += 1
            GiaTri = (MangY[iChonTT-dem])
            for j in range(len(Mang1)):
                GiaTri = Mang1[j]-GiaTri
                Mang1[j] -= GiaTri
            Mang1.append(GiaTri)
            Mang2.append(GiaTri)
        MangTong.append(Mang1[-1])
    return MangTong


def TinhTyHieu(MangY):
    return TyHieuGauss1X0(MangY), TyHieuGauss2X1(MangY)


def TinhTySaiPhan(Gauss1X0_SP, Gauss2X1_SP):
    MaTran1 = []
    for i in range(len(Gauss1X0_SP)):
        if (i % 2 == 0):
            MaTran1.append((Gauss1X0_SP[i]+Gauss2X1_SP[i])/2)
        else:
            MaTran1.append((Gauss1X0_SP[i]))
    return MaTran1


def ChanLe1(MaTran1):
    MaTran1_Chan = []
    MaTran1_Le = []
    for i in range(len(MaTran1)):
        if (i % 2 == 0):
            MaTran1_Chan.append(MaTran1[i])
        else:
            MaTran1_Le.append(MaTran1[i])

    return MaTran1_Chan, MaTran1_Le


def TinhWn_1x(SoDiemNoiSuy):
    MaTranB = np.zeros((SoDiemNoiSuy//2, SoDiemNoiSuy//2))
    MaTranB[0][-1] = 1
    for i in range(SoDiemNoiSuy//2-1):
        DaThucThuong = list(MaTranB[i])
        DaThucTich = Hoocne.NhanXTruC(DaThucThuong, ((2*i+1)/2)**2)
        DaThucTich.pop(0)
        MaTranB[i+1] = np.asarray(DaThucTich)
    return MaTranB


def ChanLe2(MaTran2):
    MaTran2_Chan = MaTran2
    MaTran2_Le = MaTran2
    return MaTran2_Chan, MaTran2_Le


def TimPt(HeSoPt_Chan, HeSoPt_Le):
    HeSoPt = []
    for i in range(len(HeSoPt_Chan)):
        HeSoPt.append(HeSoPt_Le[i])
        HeSoPt.append(HeSoPt_Chan[i])

    return HeSoPt

