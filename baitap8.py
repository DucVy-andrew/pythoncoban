
try:
    namsinh = int(input("Nhập năm sinh của bạn: "))
except:
    print("Số năm nhập vào không hợp lệ")
else:
    can = namsinh % 10
    chi = namsinh % 12
    match can:
        case 0: 
            print("Canh")
        case 1: 
            print("Tân")
        case 2: 
            print("Nhâm")
        case 3:
            print("Qúy")
        case 4: 
            print("Gíap")
        case 5: 
            print("Ất")
        case 6: 
            print("Bính")
        case 7: 
            print("Đinh")
        case 8: 
            print("Mậu")
        case 9: 
            print("Kỷ")
    match chi:
        case 0: 
            print("Thân")
        case 1: 
            print("Dậu")
        case 2: 
            print("Tất")
        case 3:
            print("Hợi")
        case 4: 
            print("Tí")
        case 5: 
            print("Sửu")
        case 6: 
            print("Dần")
        case 7: 
            print("Mão")
        case 8: 
            print("Thìn")
        case 9: 
            print("Tỵ")
        case 10: 
            print("Ngọ")
        case 11: 
            print("Mùi")
    print(f"Tính tuổi của bạn: {can + chi}")