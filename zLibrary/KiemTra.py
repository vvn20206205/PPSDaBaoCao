import CONST
# Kiểm tra dữ liệu đầu vào trước khi tính toán


def TrungDuLieu(fileMangX, fileMangY):
    print(f"\t✅ Kiểm tra trùng dữ liệu:", end='\t')
    print("(Nếu trùng => Lấy dữ liệu X[i] đầu tiên)")

    MangX = []
    MangY = []
    checkPrintKiemTraTrungDuLieu = True

    for i in range(len(fileMangX)):
        if fileMangX[i] in MangX:
            print("\t\t❎ Loại bỏ điểm trùng dữ liệu: ", end='')
            print(f"X[{i}] = {fileMangX[i]}, ", end='')
            print(f"Y[{i}] = {fileMangY[i]}")
            checkPrintKiemTraTrungDuLieu = False
        else:
            MangX.append(fileMangX[i])
            MangY.append(fileMangY[i])

    if (checkPrintKiemTraTrungDuLieu):
        print("\t[=>] Không có giá trị trùng")
    else:
        print("\t[=>]")
    print(f'\tGiá trị x: \n{MangX}')
    print(f'\tGiá trị y: \n{MangY}')
    return MangX, MangY

# SapXep


def DoiCho2PhanTuCuaMang(a, b, Mang):
    temp = Mang[a]
    Mang[a] = Mang[b]
    Mang[b] = temp


def SapXepTang(X, Y):
    # Dùng Selection Sort
    for i in range(len(X)-1):
        min_idx = i
        for j in range(i+1, len(X)):
            if (X[j] < X[min_idx]):
                min_idx = j
        DoiCho2PhanTuCuaMang(min_idx,  i, X)
        DoiCho2PhanTuCuaMang(min_idx,  i, Y)


def SapXepGiam(X, Y):
    SapXepTang(X, Y)
    X.reverse()
    Y.reverse()
# SapXep


def TangGiam(MangX, MangY):
    print(f"\t✅ Kiểm tra các mốc nội suy tăng, giảm:", end='\t')
    print("(Nếu không thỏa mãn => Có thể sắp xếp lại)")

    checkTangGiam = False

    print(f'\t\t✅ Kiểm tra tăng:')
    for i in range(1, len(MangX)):
        if (MangX[i-1] > MangX[i]):
            # Không thỏa mãn tăng thì thoát kiểm tra tăng
            print("\t\t\t❎", end=' ')
            print(f'Tại Mảng [{i-1}] = {MangX[i-1]}', end=' > ')
            print(f'{MangX[i]} = Mảng [{i}]')
            print("\t\t[=>] Không tăng")
            # Thoát kiểm tra tăng
            break
        if (i == len(MangX)-1):
            # Nếu thỏa mãn tất cả các phần tử
            # => Tăng, Không giảm kết thúc kiểm tra tăng, giảm
            checkTangGiam = True
            print("\t\t[=>] Tăng và không giảm")
            return

    print(f'\t\t✅ Kiểm tra giảm:')
    for i in range(1, len(MangX)):
        if (MangX[i-1] < MangX[i]):
            # Không thỏa mãn giảm thì thoát kiểm tra giảm
            print("\t\t\t❎", end=' ')
            print(f'Tại Mảng [{i-1}] = {MangX[i-1]}', end=' < ')
            print(f'{MangX[i]} = Mảng [{i}]')
            print("\t\t[=>] Không giảm")
            # Thoát kiểm tra giảm
            break
        if (i == len(MangX)-1):
            # Nếu thỏa mãn tất cả các phần tử
            # => Giảm kết thúc kiểm tra tăng, giảm
            checkTangGiam = True
            print("\t\t[=>] Giảm")
            return
    # Nếu không tăng, giảm
    if (not checkTangGiam):
        print("\t\t[=>] Mảng X chưa được sắp xếp!", end='')
        while True:
            print("\t\t\tChọn kiểu sắp xếp (1: tăng, -1: giảm)")
            inputSapXep = input(("\t\t\tENTER: "))
            inputSapXep = int(inputSapXep)

            if (inputSapXep == 1):
                SapXepTang(MangX, MangY)
                print(f'\tSắp xếp tăng thành công!')
                break
            elif (inputSapXep == -1):
                SapXepGiam(MangX, MangY)
                print(f'\tSắp xếp giảm thành công!')
                break
            else:
                print("\t\t\t❎ Chọn sai giá trị???", end='')


def CachDeu(MangX):
    print(f"\t✅ Kiểm tra các mốc nội suy cách đều:", end='\t')
    print("(Nếu không cách đều => Kết thúc chương trình)")

    Khoang_Cach_H = MangX[0]-MangX[1]

    for i in range(1, len(MangX)):
        if (abs(MangX[i-1] - MangX[i] - Khoang_Cach_H) > CONST.EPSILON):
            print("\t[=>] Các mốc nội suy không cách đều")
            print(f"\t[=>]", end=' ')
            print(f"Không thỏa mãn điều kiện phương pháp!", end=' ')
            print((f"Kết thúc chương trình"))
            print('✅ -'*50)
            exit()
    print("\t[=>] Các mốc nội suy có cách đều,", end="")
    print(f" Khoảng cách H = abs({Khoang_Cach_H}) = {abs(Khoang_Cach_H)}")
    return Khoang_Cach_H


def NgoaiSuy(MangX, DiemCanTinhGiaTri):
    print(f'\t✅ Kiểm tra giá trị cần tính (ngoại suy hay nội suy):')

    checkNgoaiSuy = True      # Là ngoại suy

    print(f'\t\tGiá trị cần tính: ', end='')
    print(f'{DiemCanTinhGiaTri}')

    if (MangX[0] < DiemCanTinhGiaTri):
        # a < x < b
        if (DiemCanTinhGiaTri < MangX[-1]):
            checkNgoaiSuy = False        # Là nội suy
    else:
        # a > x > b
        if (DiemCanTinhGiaTri > MangX[-1]):
            checkNgoaiSuy = False        # Là nội suy

    if (checkNgoaiSuy):
        print("\t\t❎", end=" ")
        print("Giá trị cần tính là ngoại suy!")
        print("\t\t❎ Có tiếp tục tính?(1: có, khác: không)")

        inputNgoaiSuy = input(("\t\tENTER: "))
        inputNgoaiSuy = int(inputNgoaiSuy)

        if (inputNgoaiSuy == 1):
            print("\t[=>]", end=" ")
            print("Tiếp tục chương trình:")
        else:
            print((f"Kết thúc chương trình"))
            print('✅ -'*50)
            print((f"Không tính do giá trị ngoại suy!"))
            exit()
    else:
        print("\t[=>]", end=" ")
        print("Giá trị cần tính là nội suy!")
    # input(('Nhấn ENTER để bắt đầu tính!\n'))

