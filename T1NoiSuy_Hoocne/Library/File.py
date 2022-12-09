import numpy as np
from Library import PhuongPhapSo
import MyStyle
import MyFile
import __main__ as v

TEN_PP = 'Hoocne'


def INPUT():
    # **************************************************************************************************************************************************************************************************
    # xóa màn hình Console
    MyStyle.XoaManHinh()
    # **************************************************************************************************************************************************************************************************
    lines = MyFile.DocFile(TEN_PP)

    Dong0 = lines[0].split('=')[1]
    Dong1 = lines[1].split('=')[2]
    Dong2 = lines[2].split('=')[1]

    HeSoDaThuc = (Dong0.split(' '))
    HeSoDaThuc = list(np.float_(HeSoDaThuc))

    c = float(Dong1)

    GiaTriNghiemX = (Dong2.split(' '))
    GiaTriNghiemX = list(np.float_(GiaTriNghiemX))

    return HeSoDaThuc, c, GiaTriNghiemX


def OUTPUT():
    MyFile.FolderOutput()

    # **************************************************************************************************************************************************************************************************
    strTich = 'Bảng tính Hoocne:'
    strTich += '<table style="width:100%"> <tr> <th></th>'

    for i in range(len(v.KetQua_NhanXTruC)):
        strTich += f'<th class="blue">{v.KetQua_NhanXTruC[i]}</th>'

    strTich += f'</tr> <tr> <td>x = {v.c}</td>'
    for i in range(len(v.HeSoDaThuc)):
        strTich += f'<th>{v.HeSoDaThuc[i]}</th>'

    strTich += ' <th>0 (của số dư)</th>'
    strTich += ' </tr> </table>'

    strThuong = 'Bảng tính Hoocne:'
    strThuong += '<table style="width:100%"> <tr> <th></th>'

    for i in range(len(v.HeSoDaThuc)):
        strThuong += f'<th>{v.HeSoDaThuc[i]}</th>'

    strThuong += f'</tr> <tr> <td>x = {v.c}</td>'

    for i in range(len(v.KetQua_ChiaXTruC)):
        strThuong += f'<th class="blue">{v.KetQua_ChiaXTruC[i]}</th>'

    strThuong += f' <th class="red">(Số dư, giá trị) = {v.SoDuR}</th>'
    strThuong += ' </tr> </table>'

    strWx = '= '

    for i in range(len(v.GiaTriNghiemX)):
        temp = [1.0, -v.GiaTriNghiemX[i]]
        strWx += f'({MyStyle.ConvertDaThucToString(temp)}) '

    defMyString = f"""
    <div class="input my_hide">
    <h4>DATA INPUT:</h4> 
    Hệ số đa thức đã nhập:
    <br>
    {v.HeSoDaThuc}
    <br>
    Điểm cần tính giá trị x0 = c = {v.c}
    <br>
    Các nghiệm x để tính Wn+1(x) là :
    <br>
    {v.GiaTriNghiemX}
    </div>
    <hr class="my_hide">
    <!-- ************************************************************************************************************************************************************************************************* -->
    <div class="package">
    <h3>Tính toán:</h3> 
    <h4>- Tính tích: f(x)(x-c)</h4>
    = ({MyStyle.ConvertDaThucToString(v.HeSoDaThuc)})<b class="red"> * </b>(x-{v.c})
    <br>
    {strTich}
    <div class="blue">
    = {MyStyle.ConvertDaThucToString(v.KetQua_NhanXTruC)}
    <br>
    <b >= {v.KetQua_NhanXTruC}</b></div>
    <h4>- Tính thương: f(x)/(x-c)</h4>
    = ({MyStyle.ConvertDaThucToString(v.HeSoDaThuc)})<b class="red"> / </b>(x-{v.c})
    <br>
    {strThuong}
    <b class="red">=></b> f(x) = ({MyStyle.ConvertDaThucToString(v.HeSoDaThuc)})
    <br>
    <div class="blue">
    = (x-{v.c})*({MyStyle.ConvertDaThucToString(v.KetQua_ChiaXTruC)}) + {v.SoDuR}
    <br>
    <b >= {v.KetQua_ChiaXTruC}</b></div>
    <h4>- Tính giá trị đa thức: f(c) = f(<b class="blue">{v.c}</b>)= <b class="blue">{v.KetQua_TinhGiaTri}</b></h4>
    <br>
    <h4>- Tính đạo hàm cấp 1 (Tính giá trị đa thức thương): f '(c) = f '(<b class="blue">{v.c}</b>)= <b class="blue">{v.KetQua_DaoHam1}</b></h4>
    <br>
    <h4>- Tính đạo hàm các cấp (từ 1 tới n = {len(v.KetQua_DaoHamCapCao)}): </h4>
    {v.KetQua_DaoHamCapCao} 
    <br>
    <h4>- Tính Wn+1(x)=(x-x0)(x-x1)(x-x2)...(x-n2)</h4>
    {strWx}
    <br>
    <div class="blue">
    = ({MyStyle.ConvertDaThucToString(v.KetQua_W_n_x)}) 
    <br>
    = {v.KetQua_W_n_x}</div>
    </div>
    """
    MyFile.XuatFile(TEN_PP, defMyString)
    MyStyle.ThongBaoKetThuc(TEN_PP)

