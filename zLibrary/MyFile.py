import webbrowser
import os
import numpy as np
import matplotlib.pyplot as plt
from MyStyle import XuLiString
import Hoocne
Path_OUTPUT = os.getcwd()+"\OUTPUT"


def FolderOutput():
    if (not os.path.isdir(os.path.abspath(Path_OUTPUT))):
        os.mkdir(Path_OUTPUT)


def DocFile(TEN_PP):
    print(f'- Đọc file input {TEN_PP}')
    TenFileInput = f'_{TEN_PP}_INPUT.txt'

    FileInput = open(TenFileInput, mode='r', encoding='UTF8')
    lines = FileInput.readlines()

    for i in range(len(lines)):
        lines[i] = XuLiString(lines[i])

    j = 0
    for i in range(len(lines)):
        if ('**********' in lines[i]):
            j = i
            break
    if (j == 0):
        return lines
    else:
        return lines[j+1:]


def XuatFile(TEN_PP, str_INPUT):

    TenFileOutput = f'{Path_OUTPUT}\zhtml_{TEN_PP}_OUTPUT.html'
    file = open(TenFileOutput, mode='w', encoding='UTF8')

    MyString = f"""
<!DOCTYPE html>
<html lang="vn">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Phương pháp: {TEN_PP}</title>
<link rel="stylesheet" href="../Library/_style.css">
</head>
    
<body>
<hr> 
<a href="zThuatToan.txt"><header>Phương pháp: {TEN_PP}</header></a>
<hr> 
 
{str_INPUT}

<hr> 
<footer>Vũ Văn Nghĩa 20206205</footer>
<hr> 
</body>
</html>
    """

    file.write(MyString)
    file.close()
    webbrowser.open(TenFileOutput)


def MyMatplotlib(fileMangX, fileMangY, HeSoFx, TEN_PP):

    # Chức năng: tính giá trị x, y phục vụ vẽ hình
    xpoints = np.array(fileMangX)
    ypoints = np.array(fileMangY)
    plt.plot(xpoints, ypoints, 'o', color='red')
    # vẽ các chấm đỏ

    min_x = min(fileMangX)-1
    max_x = max(fileMangX)+1
    x = np.linspace(min_x, max_x, 1000)
    y = Hoocne.TinhGiaTri(HeSoFx, x)
    plt.plot(x, y, color='blue')
    # vẽ đồ thị

    plt.title(f'{TEN_PP}')
    plt.savefig(f'{Path_OUTPUT}\zpng_{TEN_PP}_OUTPUT.png')
    # plt.show()

