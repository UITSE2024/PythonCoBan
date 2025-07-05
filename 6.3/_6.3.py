def ChuanHoaXau(ss):
    words = ss.split()
    ss = [word.capitalize() for word in words]
    return ' '.join(ss)

s = input("Nhap chuoi: ")
print(ChuanHoaXau(s))
