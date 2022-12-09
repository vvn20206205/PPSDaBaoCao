import CONST
import numpy as np
import Hoocne


def ChonTrungTam(MangX, DiemCanTinhGiaTri, GiaTriDiemTT):
    # Thuật toán
    iChon = 0
    if (GiaTriDiemTT == 0):
        # bằng 0: Tìm mốc nội suy gần giá trị cần tính
        min = DiemCanTinhGiaTri
        for i in range(len(MangX)):
            if (min > abs(MangX[i]-DiemCanTinhGiaTri)):
                min = abs(MangX[i]-DiemCanTinhGiaTri)
                iChon = i
    else:
        # khác 0: Mốc nội suy trung tâm từ file input
        for i in range(len(MangX)):
            if (abs(MangX[i]-GiaTriDiemTT) < CONST.EPSILON):
                iChon = i
                break
    # Thuật toán

    # OUTPUT_STRING
    if (True):
        OUT_String = """
            <h4>- Gói 0: Chọn index mốc nội suy trung tâm</h4>
        """
        if (GiaTriDiemTT == 0):
            OUT_String += f"""
                \tCHỌN ĐIỂM NỘI SUY TRUNG TÂM PHÙ HỢP VỚI ĐIỂM CẦN TÍNH GIÁ TRỊ:
                <b class="red">(X NGANG = {DiemCanTinhGiaTri})</b>
            """
        else:
            OUT_String += f"""
                \tĐIỂM NỘI SUY TRUNG TÂM ĐÃ CHỌN TRONG FILE:
                <b class="red">(TRUNG TÂM = {GiaTriDiemTT})</b>
            """
        GiaTriDiemTT = MangX[iChon]
        OUT_String += f"""
                \n<br>
                \n=> ĐIỂM NỘI SUY TRUNG TÂM: <b class="blue">{GiaTriDiemTT}</b>
            """
    # OUTPUT_STRING

    return iChon, OUT_String


def ToiUuMoc(MangX, MangY, iChonTT):
    print("✅Chọn các mốc phù hợp với PP")
    if (iChonTT == len(MangX)-iChonTT-1):
        print("✅Không cần tối ưu mốc")
        return MangX, MangY

    if (iChonTT < len(MangX)-iChonTT-1):
        print("✅Bên trái có ít hơn")
        MangX = (MangX[:(2*iChonTT+1)])
        MangY = (MangY[:(2*iChonTT+1)])
        return MangX, MangY

    if (iChonTT > len(MangX)-iChonTT-1):
        print("✅Bên phải có ít hơn")
        MangX = (MangX[(iChonTT - (len(MangX)-iChonTT-1)):])
        MangY = (MangY[(iChonTT - (len(MangY)-iChonTT-1)):])
        return MangX, MangY


def TinhTyHieu(MangY):
    iChonTT = len(MangY)//2

    Mang1 = [MangY[iChonTT]]
    Mang2 = [MangY[iChonTT]]
    MangTong = [MangY[iChonTT]]

    for i in range(1, iChonTT+1):
        # Xét x1,x2,x3,x4,x5,...
        GiaTri = MangY[iChonTT+i]
        for j in range(len(Mang2)):
            GiaTri -= Mang2[j]
            Mang2[j] += GiaTri
        Mang1.append(GiaTri)
        Mang2.append(GiaTri)
        # Xét x-1,x-2,x-3,x-4,x-5,...
        GiaTri = (MangY[iChonTT-i])
        for j in range(len(Mang1)):
            GiaTri = Mang1[j]-GiaTri
            Mang1[j] -= GiaTri
        Mang1.append(GiaTri)
        Mang2.append(GiaTri)

        MangTong.append((Mang1[-2]+Mang2[-2])/2)
        MangTong.append(Mang1[-1])
    return MangTong


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
    MaTranB = np.zeros((SoDiemNoiSuy//2+1, SoDiemNoiSuy//2+1))
    MaTranB[0][-1] = 1
    for i in range(SoDiemNoiSuy//2):
        DaThucThuong = list(MaTranB[i])
        DaThucTich = Hoocne.NhanXTruC(DaThucThuong, i*i)
        DaThucTich.pop(0)
        MaTranB[i+1] = np.asarray(DaThucTich)

    return MaTranB


def ChanLe2(MaTran2):
    MaTran2_Chan = MaTran2
    MaTran2_Le = []
    for i in range(len(MaTran2)):
        if (i == 0):
            continue
        temp = list(MaTran2[i])
        temp.pop(-1)
        MaTran2_Le.append(temp)
    MaTran2_Le = np.array(MaTran2_Le)

    return MaTran2_Chan, MaTran2_Le


def TimPt(HeSoPt_Chan, HeSoPt_Le):
    HeSoPt = []
    for i in range(len(HeSoPt_Chan)):
        if (i == len(HeSoPt_Chan)-1):
            HeSoPt.append(HeSoPt_Chan[i])
            break
        HeSoPt.append(HeSoPt_Chan[i])
        HeSoPt.append(HeSoPt_Le[i])

    return HeSoPt

