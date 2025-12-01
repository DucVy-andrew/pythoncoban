def intamgiacsao(n):
    print("======================")
    print("======== BÀI 13 ======")
    print("====In tam giác sao===")
    print()
    str = "*"
    for i in range(1,n+1):
        ketqua = print(f"{i * str}")
    return ketqua

def kiemtrasohoanhao(n):
    print("=================================================")
    print("==================== BÀI 11 =====================")
    print("====Kiểm tra một số có phải số hoàn hảo không.===")
    print()
    t = 0
    for i in range(1,n):
        if n % i == 0:
            t += i
    if t == n:
        ketqua = print(f"{n} là số hoàn hảo")
    else:
        ketqua = print(f"{n} là số không hoàn hảo")  
    return ketqua
                