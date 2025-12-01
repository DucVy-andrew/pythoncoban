# 4. Nhập 10 số từ bàn phím, đếm xem có bao nhiêu số âm.
i = 1
ketqua = 0
while i <= 10:
    try:
        n = int(input(f"Nhập vào số thứ {i}: "))
        i += 1
        if n < 0:
            ketqua +=1
    except:
        print(f"Dữ liệu đưa vào không hợp lệ, vui lòng chỉ nhập số")
print(f"Tổng có {ketqua} số âm"); 