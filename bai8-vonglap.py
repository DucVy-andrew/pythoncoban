print("=======Câu 8==========")
while True:
    try:
        n = int(input("Nhập số lượng số muốn tìm: "))
        if n < 1:
            print("Nhập số nguyên dương và lớn hơn (0)")
        if n > 0:
            break
    except:
        print("Lỗi nhập liệu, vui lòng thử lại")

print("Nhập n số, tìm số lớn nhất và nhỏ nhất ")
i = 1
max = -1000
min = 1000
while i <= n:
    try:
        so = int(input(f"Nhập số thứ {i}: "))
        i+= 1
        if(so > max):
            max = so
        if(so < min):
            min = so
    except ValueError:
        print("Lỗi nhập liệu, vui lòng nhập lại")
print(f"Số lớn nhất là {max}")
print(f"Số bé nhất là: {min}")