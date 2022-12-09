import os
import Hoocne
import CONST


def XoaManHinh():
    os.system('cls')


def ThongBaoKetThuc(TEN_PP):
    print(f'✅ Chạy chương trình {TEN_PP} thành công!')


def XuLiString(StringCanXuLi):
    # Chức năng: Xử lí string trong file
    StringCanXuLi = StringCanXuLi.strip()
    # Xóa [,] nếu có
    StringCanXuLi = StringCanXuLi.replace('[', '')
    StringCanXuLi = StringCanXuLi.replace(']', '')
    # Xóa 2 space nếu có
    while '  ' in StringCanXuLi:
        StringCanXuLi = StringCanXuLi.replace('  ', ' ')
    # Xóa space sau dấu trừ nếu có
    StringCanXuLi = StringCanXuLi.replace('- ', '-')
    # Xóa space sau dấu = nếu có
    StringCanXuLi = StringCanXuLi.replace('= ', '=')

    return StringCanXuLi


def ConvertDaThucToString(listHeSo, x='x'):
    # Chức năng: Chuyển hệ số thành chuỗi đa thức
    str_OUTPUT = ''
    if (len(listHeSo) == 1):
        str_OUTPUT += f'{listHeSo[0]}'
        return str_OUTPUT
    if (len(listHeSo) == 2):
        match listHeSo[0]:
            case 1:
                str_OUTPUT += f'{x}'
            case -1:
                str_OUTPUT += f'-{x}'
            case _:
                str_OUTPUT += f'{(listHeSo[0])}{x}'
    else:
        str_OUTPUT += f'{listHeSo[0]}{x}^{len(listHeSo)-1}'

    if (listHeSo[1] >= 0):
        str_OUTPUT += '+'
    temp_listHeSo = list(listHeSo)
    temp_listHeSo.pop(0)
    return str_OUTPUT + ConvertDaThucToString(temp_listHeSo, x)


def KiemTraLaiGiaTri(MangX, MangY, HeSoFx):
    string = f'<pre>'
    string += f'<b class="red">✅ Kiểm tra lại: EPSILON = { CONST.EPSILON}</b>'
    string += '\n'

    for i in range(len(MangX)):
        GiaTri = Hoocne.TinhGiaTri(HeSoFx, MangX[i])

        string += f'{MangX[i]}'+' '*(8-len(f'{MangX[i]}'))
        string += f'|   {MangY[i]} = {GiaTri}'
        string += ' ' * (35-len(f'|   {MangY[i]} = {GiaTri}'))+'|'
        string += '\n'

        if (abs(MangY[i] - GiaTri) > CONST.EPSILON):
            string += '<b class="red">=> Sai ❎</b>'
            string += f'<pre>'
            return string

    string += '<b class="blue">=> Đúng ✅</b>'
    string += f'<pre>'
    return string

