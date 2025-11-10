# Cấu trúc điều khiển if_else

try:
    n = int(input('Nhập vào một số nguyên dương: '))
except:
    print('Lỗi nhập liệu')
else:
    if n > 0:
        if n % 2 == 0:
            print(f"{n} là số chẵn")
        else:
            print(f"{n} là số lẻ")
    else:
        print("Không hợp lệ, nhập số nguyên dương , số lớn hơn 0")