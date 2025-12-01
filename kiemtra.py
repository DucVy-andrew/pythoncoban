# Gọi hàm
import kiemtra_func

# Kiểm tra dữ liệu đầu vào
while True:
    try:
        n = int(input("Nhập vào N: "))
        if n == 0:
            print("Vui lòng nhập số lớn hơn (0) ")
        if n > 0:
            break
    except ValueError:
        print("Vui lòng nhập số nguyên !")    

# Câu 11
kiemtra_func.intamgiacsao(n)

# Câu 13
kiemtra_func.kiemtrasohoanhao(n)
 
        