try:
    thang = int(input("Nhập tháng: "))
except:
    print("Dữ liệu không hợp lệ")
else:
    match thang:
        case 1|3|5|7|8|10|12:
            print("Tháng này có 31 ngày")
        case 4|6|9|11:
            print('Tháng này có 30 ngày')
        case 2:
            nam = int(input("Nhập năm: "))
            if(nam % 4 == 0):
                print("Tháng 2 năm này có 29 ngày")
            else:
                print("Tháng 2 này có 28 ngày")
        case _:
            print("Số tháng không hợp lệ")
