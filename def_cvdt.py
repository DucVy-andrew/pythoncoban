import def_func_cvdt

print("TÍNH CHU VI DIỆN TÍCH HÌNH CHỮ NHẬT")
while True:
    try:
        chieudai = int(input("Nhập chiều dài: "))
        chieurong = int(input("Nhập chiều rộng: "))
        if chieudai == 0 or chieurong == 0:
            print("Độ dài các cạnh phải lớn hơn (0) vui lòng kiểm tra lại")
        if chieudai > 0 and chieurong > 0:
            break
    except:
        print("Loi nhap lieu")
   
def_func_cvdt.cvdt(chieudai,chieurong)
