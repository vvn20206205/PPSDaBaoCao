from Library import *
import Hoocne
# MAIN bắt đầu
# if __name__ == '__main__':
# **************************************************************************************************************************************************************************************************
# ! Đọc input từ file
HeSoDaThuc, c, GiaTriNghiemX = File.INPUT()
# Từ file input => return (HeSoDaThuc, c, GiaTriNghiemX)
# ! Tính toán
# **************************************************************************************************************************************************************************************************
KetQua_NhanXTruC = Hoocne.NhanXTruC(HeSoDaThuc, c)

KetQua_ChiaXTruC, SoDuR = Hoocne.ChiaXTruC(HeSoDaThuc, c)

KetQua_TinhGiaTri = Hoocne.TinhGiaTri(HeSoDaThuc, c)

KetQua_DaoHam1 = Hoocne.DaoHam1(HeSoDaThuc, c)

KetQua_DaoHamCapCao = Hoocne.DaoHamCapCao(HeSoDaThuc, c)

KetQua_W_n_x = Hoocne.W_n_x(GiaTriNghiemX)
# **************************************************************************************************************************************************************************************************
# ! Xuất kết quả
File.OUTPUT()
