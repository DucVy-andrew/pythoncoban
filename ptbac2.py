import math
# Tính phương trình bậc 2
print("GIẢI PHƯƠNG TRÌNH BẬC 2")
a = int(input("Nhập vào giá trị a: "))
b = int(input("Nhập vào giá trị b: "))
c = int(input("Nhập vào giá trị c: "))
delta = int((b**2) - (4*a*c))

if delta < 0:
    print("Vô nghiệm")
elif delta == 0:
    x = (-b)/(2*a)
    print(f"X có giá trị là {x}")
else:
    x1 = ((-b) + math.sqrt(delta)) / 2*a
    x2 = ((-b) - math.sqrt(delta)) / 2*a
    print(f"X1 có giá trị là {x1}")
    print(f"X2 có giá trị là {x2}")

