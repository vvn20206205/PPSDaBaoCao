from Library import *
import KiemTra
import PhepTinh
import Hoocne
import Sterlin
# MAIN bắt đầu
# if __name__ == '__main__':
# **************************************************************************************************************************************************************************************************
# ! Đọc input từ file
fileMangX, fileMangY, DiemCanTinhGiaTri, GiaTriDiemTT = File.INPUT()
# Từ file input => return (fileMangX,fileMangY,DiemCanTinhGiaTri, GiaTriDiemTT)
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
# ! Gói 0: Chọn index mốc nội suy trung tâm và Chọn các mốc phù hợp với PP
# Chọn index mốc nội suy trung tâm
iChonTT, STRING0 = Sterlin.ChonTrungTam(MangX, DiemCanTinhGiaTri, GiaTriDiemTT)
GiaTriDiemTT = MangX[iChonTT]
# Chọn các mốc phù hợp với PP
# Số mốc lẻ và đi đều từ trung tâm về 2 phía
MangX, MangY = Sterlin.ToiUuMoc(MangX, MangY, iChonTT)
print(f'\tGiá trị x: \n{MangX}')
print(f'\tGiá trị y: \n{MangY}')
# **************************************************************************************************************************************************************************************************
# ! Gói 1: Tính tỷ hiệu, tỷ sai phân
# Tính tỷ hiệu
MaTranA = Sterlin.TinhTyHieu(MangY)
# Tính tỷ sai phân
# Lấy tỷ hiệu chia cho giai thừa
MaTran1 = PhepTinh.TinhTySaiPhan(MaTranA)
# Tìm phần chẵn, phần lẻ
MaTran1_Chan, MaTran1_Le = Sterlin.ChanLe1(MaTran1)
# **************************************************************************************************************************************************************************************************
# ! Gói 2: Tính Wn_1x
MaTran2 = Sterlin.TinhWn_1x(len(MangX))
# Tìm phần chẵn, phần lẻ
MaTran2_Chan, MaTran2_Le = Sterlin.ChanLe2(MaTran2)
# **************************************************************************************************************************************************************************************************
# ! Gói 3: Tìm P(t)
# Tìm phần chẵn, phần lẻ
HeSoPt_Chan = PhepTinh.Nhan2MaTran(MaTran1_Chan, MaTran2_Chan)
HeSoPt_Le = PhepTinh.Nhan2MaTran(MaTran1_Le, MaTran2_Le)
# ! => Tìm P(t)
HeSoPt = Sterlin.TimPt(HeSoPt_Chan, HeSoPt_Le)
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
