# Chương trình tính tiền taxi

km = int(input("Nhập số km bạn đã đi: "))

if km > 0 and km < 2:
    money = km * 20
elif km >= 2 and km <= 5:
    money = (1 * 20) + ((km - 1) * 16)
elif km >= 6 and km <= 10:
    money = (1 * 20) + (4 * 16) + ((km - 5) * 13)
elif km > 10:
    money = (1 * 20) + (4 * 16) + (5 * 13) + ((km - 10) * 10)
else:
    money = 0
    print("Số km không hợp lệ!")

# In kết quả
if money > 0:
    print(f"Số tiền phải trả là: {money} nghìn đồng")
    if money > 200000:
        payoff = money * 10 / 100
        last_money = money - payoff
        print(f"Số tiền bạn phải trả là: {last_money} nghìn đồng")
