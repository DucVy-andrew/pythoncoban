import math
a = float(input("Nhập giá trị cho a: "))
b = float(input("Nhập giá trị cho b: "))
c = float(input("nhập giá trị chi c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Độ dài cạnh không hợp lệ, vui lòng kiểm tra lại")
else:
    if (a + b > c) and (a + c > b) and (a + b > a):
        cv = a + b + c
        p =  float(cv / 2)
        dt = float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
        print(f"Chu vi hình tam giác là: {cv}")
        print(f"Diện tích hình tam giác là: {dt}")
    else:
        print("Kích thước số đo các các cạnh chưa hợp lệ, vui lòng kiểm tra lại")