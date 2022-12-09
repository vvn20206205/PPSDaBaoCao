import numpy as np
import os
from Library import PhuongPhapSo
import MyStyle
import MyFile
import __main__ as v

TEN_PP = 'Bessel'


def INPUT():
    # **************************************************************************************************************************************************************************************************
    # xóa màn hình Console
    MyStyle.XoaManHinh()
    # **************************************************************************************************************************************************************************************************
    lines = MyFile.DocFile(TEN_PP)

    Dong0 = lines[0].split('=')[1]
    DiemCanTinhGiaTri = float(Dong0)

    Dong1 = lines[1].split('=')[1]
    GiaTriDiemTT = (Dong1.split(';'))
    GiaTriDiemTT0 = float(GiaTriDiemTT[0])
    GiaTriDiemTT1 = float(GiaTriDiemTT[1])

    # bỏ qua
    Dong2 = lines[2]

    fileMangX = []
    fileMangY = []
    for i in range(3, len(lines)):

        x_temp = float(lines[i].split(' ')[0])
        y_temp = float(lines[i].split(' ')[1])
        fileMangX.append(x_temp)
        fileMangY.append(y_temp)
    return fileMangX, fileMangY, DiemCanTinhGiaTri, GiaTriDiemTT0, GiaTriDiemTT1


def OUTPUT():
    MyFile.FolderOutput()

    # **************************************************************************************************************************************************************************************************
    # Vẽ hình
    fileMangT = list(v.fileMangX)
    for i in range(len(v.fileMangX)):
        temp = - (v.fileMangX[i]-v.GiaTriDiemTT)
        temp /= v.Khoang_Cach_H
        fileMangT[i] = temp
    MyFile.MyMatplotlib(fileMangT, v.fileMangY, v.HeSoPt, TEN_PP)
# **************************************************************************************************************************************************************************************************
    # Kiểm tra lại
    MangT = list(v.MangX)
    for i in range(len(v.MangX)):
        temp = -(v.MangX[i]-v.GiaTriDiemTT)
        temp /= v.Khoang_Cach_H
        MangT[i] = temp
    STRING1 = MyStyle.KiemTraLaiGiaTri(MangT, v.MangY, v.HeSoPt)
# **************************************************************************************************************************************************************************************************
    def_Chung = f"""
    <div class="flex-container">
    <hr class="my_hide">
        <div class="w30 my_hide">  
            <div class="input">
                <h4>DATA INPUT:</h4> 
                Điểm cần tính giá trị: X ngang = {v.DiemCanTinhGiaTri}
                <br>
                Giá trị x input:
                <br>
                {v.fileMangX}
                <br>
                Giá trị y input:
                <br>
                {v.fileMangY}
            </div>
     <hr> 
            <div class="input_checked">
                <div class="package package0">
                {v.STRING0}
                </div>

                Các mốc nội suy dùng để tính toán:
                <br>
                Giá trị x chọn:
                <br>
                {v.MangX}
                <br>
                Giá trị y tương ứng:
                <br>
                {v.MangY}
                <br>
                => Số mốc nội suy đã chọn: {len(v.MangX)},
                Bậc của đa thức nội suy: {len(v.MangX)-1}
            </div>
   <hr> 
            <div class="img">
                <a href="{os.path.abspath(f"zpng_{TEN_PP}_OUTPUT.png")}">
                <img width="450px"  src="zpng_{TEN_PP}_OUTPUT.png" alt="Đồ thị {TEN_PP}">
                </a>
            </div>
    <hr>
            <div class="test">
                {STRING1}
            </div> 
        <div > 
    </div> 

    </div>
  <hr class="my_hide">
<!-- ************************************************************************************************************************************************************************************************* -->
    """

    def_MyString = f"""
    {def_Chung}
    <div id="w70"> 
<div class="package package1">
 <h4>- Gói 1: Tính tỷ hiệu, tỷ sai phân</h4>


<table style="width:100%">
    <tr>
        <th colspan="2"><h5>- Kết quả tỷ hiệu:</h5></th>
    </tr>

    <tr>
        <td> <h5>Gói Gauss1 theo x0</h5></td>
        <td> <h5>Gói Gauss2 theo x1</h5></td>
    </tr> 
   
    <tr>
        <td>  <p class="blue">{v.Gauss1X0}</p></td>
        <td>  <p class="blue">{v.Gauss2X1}</p></td>
    </tr> 
            
    <tr>
        <th colspan="2"> <h5>- Tỷ sai phân (Sau khi lấy tỷ hiệu chia cho giai thừa):</h5></th>
    </tr>
   
    <tr>
        <td>     <p class="blue">{v.Gauss1X0_SP}</p></td>
        <td>  <p class="blue">{v.Gauss2X1_SP}</p> </td>
    </tr>
       
    <tr>
        <th colspan="2"> <h5>=> Tính tỷ sai phân Bessel=(Gauss1+Gauss2)/2:</h5></th>
    </tr>
            
    <tr>
        <th colspan="2">     <p class="blue">{v.MaTran1}</p></th>
    </tr>
</table>
 
    <h5>- Tìm phần chẵn,phần lẻ:</h5>
    <h5>=> (Hệ số chẵn) \tMaTran1_Chan:</h5>
    <p class="blue">{v.MaTran1_Chan}</p>
    <h5>=> (Hệ số lẻ)   \tMaTran1_Le:</h5>
    <p class="blue">{v.MaTran1_Le}</p>
</div>


<div class="package package2">
    <h4>- Gói 2: Tính ma trận các tích W_n+1_(x)</h4>
    <table style="width:100%">
    <tr>
    <th>Tính W_n+1_(x)</th>
    <th colspan="2">=> Tìm phần chẵn,phần lẻ:</th>
    </tr>
    <tr>
    <td><h5>Kết quả gói 2: </h5></td>
    <td><h5>- (Hệ số chẵn) MaTran2_Chan: </h5></td>
    <td><h5>- (Hệ số lẻ) MaTran2_Le:</h5></td>
    </tr>
    <tr>
    <td><pre><p class="blue">{v.MaTran2}</p></pre></td>
    <td><pre><p class="blue">{v.MaTran2_Chan}</p></pre></td>
    <td><pre><p class="blue">{v.MaTran2_Le}</p></pre></td>
    </tr>
    </table>
</div>

<div class="package package3">
    <h4>- Gói 3: Tìm P(t):\t(Với T = (X_k-X_tt)/H)</h4>
    <h5>Kết quả:</h5>
    <h5>Tìm phần chẵn,phần lẻ:</h5>
    <h5>=> (Hệ số chẵn) \tHeSoPt_Chan:</h5>
    <p class="blue">{v.HeSoPt_Chan}</p>
    <h5>=> (Hệ số lẻ)   \tHeSoPt_Le:</h5>
    <p class="blue">{v.HeSoPt_Le}</p>
    <h5>=> Hệ số Pt:</h5>
    <p class="blue">{v.HeSoPt}</p>
</div>



<div class="package packageKQ">
    <h5>=> Kết quả:</h5>
    <h5>
    P(t) =
    </h5>
    <p class="blue">   {MyStyle.ConvertDaThucToString(v.HeSoPt,'t')}</p>
    <h5>=> Hệ số Pt:</h5>
    <p class="blue">   {v.HeSoPt}</p>
    <h5>=> Giá trị nội suy f(x) =
    f(<b class="blue">{v.DiemCanTinhGiaTri}</b>) =
    P(<b class="blue">{v.DiemCanTinhGiaTri2}</b>) =
    <b class="blue">{v.GiaTriKetQuaPt}</b>
    </h5>
</div>
        </div>
    </div>
    </div>
    </div>
    </div>
    """

    MyFile.XuatFile(TEN_PP, def_MyString)
    MyStyle.ThongBaoKetThuc(TEN_PP)

