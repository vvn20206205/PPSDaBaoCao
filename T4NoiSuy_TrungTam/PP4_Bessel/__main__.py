from Library import *
import KiemTra
import PhepTinh
import Hoocne
import Bessel
# MAIN bắt đầu
# if __name__ == '__main__':
# **************************************************************************************************************************************************************************************************
# ! Đọc input từ file
fileMangX, fileMangY, DiemCanTinhGiaTri, GiaTriDiemTT0, GiaTriDiemTT1 = File.INPUT()
# Từ file input => return (fileMangX,fileMangY,DiemCanTinhGiaTri, GiaTriDiemTT0, GiaTriDiemTT1)
# **************************************************************************************************************************************************************************************************
# ☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑
# ! Kiểm tra các điều kiện
# ☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑
# ! Kiểm tra trùng dữ liệu
# Nếu trùng => Lấy dữ liệu X[i] đầu tiên
MangX, MangY = KiemTra.TrungDuLieu(fileMangX, fileMangY)
# ☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑
# ! Kiểm tra các mốc nội suy tăng, giảm
# Nếu (không tăng và không giảm) => Có thể sắp xếp lại
KiemTra.TangGiam(MangX, MangY)
print(("\t[=>]"))
print(f'\tGiá trị x: \n{MangX}')
print(f'\tGiá trị y: \n{MangY}')
# ☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑
# ! Kiểm tra các mốc nội suy cách đều
# Nếu không cách đều => Kết thúc chương trình
Khoang_Cach_H = KiemTra.CachDeu(MangX)
# ☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑
# ! Kiểm tra giá trị cần tính (ngoại suy hay nội suy)
# Nếu là ngoại suy
# 1: Vẫn chạy chương trình
# 2: Kết thúc chương trình!
KiemTra.NgoaiSuy(MangX, DiemCanTinhGiaTri)
# ☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑☑
# **************************************************************************************************************************************************************************************************
# ! Gói 0: Chọn index mốc nội suy trung tâm (x0) và Chọn các mốc phù hợp với PP
iChonTT, STRING0 = Bessel.ChonTrungTam(
    MangX, DiemCanTinhGiaTri, GiaTriDiemTT0, GiaTriDiemTT1)
GiaTriDiemTT0 = MangX[iChonTT]
GiaTriDiemTT1 = MangX[iChonTT+1]
GiaTriDiemTT = (GiaTriDiemTT0+GiaTriDiemTT1)/2
# Chọn các mốc phù hợp với PP
# Số mốc chẵn và đi đều từ trung tâm về 2 phía
MangX, MangY = Bessel.ToiUuMoc(MangX, MangY, iChonTT)
print(f'\tGiá trị x: \n{MangX}')
print(f'\tGiá trị y: \n{MangY}')
# **************************************************************************************************************************************************************************************************
# ! Gói 1: Tính tỷ hiệu, tỷ sai phân
# Tính tỷ hiệu
Gauss1X0, Gauss2X1 = Bessel.TinhTyHieu(MangY)
# Tính tỷ sai phân
# Lấy tỷ hiệu chia cho giai thừa
Gauss1X0_SP = PhepTinh.TinhTySaiPhan(Gauss1X0)
Gauss2X1_SP = PhepTinh.TinhTySaiPhan(Gauss2X1)
# Tính tỷ sai phân Bessel=(Gauss1+Gauss2)/2
MaTran1 = Bessel.TinhTySaiPhan(Gauss1X0_SP, Gauss2X1_SP)
# Tìm phần chẵn, phần lẻ
MaTran1_Chan, MaTran1_Le = Bessel.ChanLe1(MaTran1)
# **************************************************************************************************************************************************************************************************
# ! Gói 2: Tính Wn_1x
MaTran2 = Bessel.TinhWn_1x(len(MangX))
# Tìm phần chẵn, phần lẻ
MaTran2_Chan, MaTran2_Le = Bessel.ChanLe2(MaTran2)
# **************************************************************************************************************************************************************************************************
# ! Gói 3: Tìm P(t)
# Tìm phần chẵn, phần lẻ
HeSoPt_Chan = PhepTinh.Nhan2MaTran(MaTran1_Chan, MaTran2_Chan)
HeSoPt_Le = PhepTinh.Nhan2MaTran(MaTran1_Le, MaTran2_Le)
# ! => Tìm P(t)
HeSoPt = Bessel.TimPt(HeSoPt_Chan, HeSoPt_Le)
# **************************************************************************************************************************************************************************************************
# ! Tính giá trị điểm cần tính
# T = (X_k-X_tt)/H
DiemCanTinhGiaTri2 = (DiemCanTinhGiaTri-GiaTriDiemTT)
DiemCanTinhGiaTri2 /= abs(Khoang_Cach_H)
GiaTriKetQuaPt = Hoocne.TinhGiaTri(HeSoPt, DiemCanTinhGiaTri2)
# **************************************************************************************************************************************************************************************************
# ! Xuất kết quả
File.OUTPUT()
# **************************************************************************************************************************************************************************************************
