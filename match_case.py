month = int(input("Nhập số tháng: "))

match month:
    case 1|2|3:
        print("Mùa xuân")
    case 4|5|6:
        print("Mùa hạ")
    case 7|8|9:
        print("Mua thu")
    case 10|11|12:
        print("Mua đông")
    case _:
        print("Tháng không hợp lệ !")

