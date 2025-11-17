try:
    van = float(input("Nhập điểm văn: "))
    toan = float(input("Nhập điểm toán: "))
    anh = float(input("Nhập điểm anh văn: "))
except ValueError:
    print("Lỗi nhập liệu")
else:
    if (van < 0 or van > 10) or (toan < 0 or toan > 10) or (anh < 0 or anh > 10):
        print("Chỉ cho phép nhập điểm từ 0 đến 10")
    else:
        dtb = (van + toan + anh) / 3
        if dtb >= 9:
            print("Học sinh xuất sắc")
        elif dtb >= 8:
            print("Học sinh giỏi")
        elif dtb >= 7:
            print("Học sinh khá")
        elif dtb >= 5:
            print("Học sinh trung bình")
        else:
            print("Học sinh yếu")