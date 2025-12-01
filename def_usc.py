import def_func_usc
while True:
    try:
        a = int(input("Nhap a: "))
        b = int(input("Nhap b: "))
        if a == 0 or b == 0:
            print("Vui lòng nhập số lớn hơn (0)")
        if a > 0 and b > 0:
            break
    except:
        print("Lỗi nhập liệu")

print(f"Uoc so chung lon nhat {def_func_usc.uscln(a,b)}")
