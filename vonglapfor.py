# 1. In các số từ 1 đến n nhưng chỉ in số chẵn.
# 2. Tính tổng các số từ 1 đến n nhưng chỉ cộng số lẻ.
# 3. Đếm có bao nhiêu số chia hết cho 3 trong đoạn [1, n].
# 4. Nhập 10 số từ bàn phím, đếm xem có bao nhiêu số âm.
# 5. In bảng cửu chương của một số n (1–10).
# 6. Nhập n, in ra các số từ 1 đến n nhưng bỏ qua số 5 (skip bằng continue).
# 8. Nhập n số, tìm số lớn nhất và nhỏ nhất.

#==========================================================================
while True:
    try:
        n = int(input("Nhập vào số ngẫu nhiên N: "))
        if n > 0:
            break
        if n < 1:
            print("Nhập số nguyên dương và lớn hơn (0)")
    except:
        print("Dữ liệu nhập vào không hợp lệ ! , vui lòng chỉ nhập số dương")
print() 
print("=======Câu 1==========")
print("In các số từ 1 đến n nhưng chỉ in số chẵn")
for i in range(1,n+1):
    if i % 2 == 0:
        print(f"{i}",end=" ")
print()  
print("=======Câu 2==========")
print("Tính tổng các số từ 1 đến n nhưng chỉ cộng số lẻ")
t = 0
for i in range(1,n+1):
    if i % 2 !=0:
        t += i
print(f"Tổng là: {t}")
print() 
print("=======Câu 3==========")
print("Đếm có bao nhiêu số chia hết cho 3 trong đoạn [1, n]")
so = 0
for i in range(1,n+1):
    if i % 3 == 0:
        so += 1
print(f"Tổng có ({so}) chia hết cho 3")
print() 
print("=======Câu 5==========")
print("In bảng cửu chương của một số n (1–10)")
print(f"Bảng cửu chương {n}")
for i in range(1,11):
    ketqua = i * n
    print(f"{i} * {n} = {ketqua}")
print() 
print("=======Câu 6==========")
print("Nhập n, in ra các số từ 1 đến n nhưng bỏ qua số 5 (skip bằng continue)")
for i in range(1,n+1):
    if(i % 5 == 0):
        continue
    print(f"{i}",end= " ")
print() 
print("=======Câu 7==========")
print("Tính tổng các số nguyên tố nhỏ hơn n")
tong = 0
for i in range(1,n+1):
    if i < n:
        tong += i

print(f"Tổng các số bé hơn N: {tong}")
print("=======Câu 9==========")
print("Đếm số chữ số của một số nguyên dương (không dùng str). và in ra số đảo của chính nó")
so = n
demchuso = 0
while so != 0:
    so = so//10
    demchuso +=1
print(f"Số {n} có {demchuso} chữ số")
print()
print("=======Câu 10==========")
print("Fibonacci")
for i in range(1,n + 1):