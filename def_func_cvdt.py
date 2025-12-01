print("TÍNH CHU VI DIỆN TÍCH HÌNH CHỮ NHẬT")

# def dientichhcn(chieudai,chieurong):
#     dientich = chieudai * chieurong
#     print(f"dien tich chn: {dientich}")

# def chuvihcn(chieudai,chieurong):
#     chuvi = (chieudai + chieurong) * 2
#     print(f"chu vi hcn: {chuvi}")

# dientichhcn(chieudai,chieurong)
# chuvihcn(chieudai,chieurong)

def cvdt(chieudai,chieurong):
    cv = (chieudai + chieurong) * 2
    dt = (chieudai * chieurong)
    ketqua = (cv,dt)
    hienthi = print(f"Chu vi la: {ketqua[0]} , dien tich la: {ketqua[1]}")
    return hienthi

