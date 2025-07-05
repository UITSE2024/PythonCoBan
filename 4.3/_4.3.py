
def HieuChuan(hh, mm, ss):
    time = hh * 3600 + mm * 60 + ss
    hh = time // 3600
    mm = (time % 3600) // 60
    ss = time % 60
    return hh, mm, ss

h = int(input("Nhap gio: "))
m = int(input("Nhap phut: "))
s = int(input("Nhap giay: "))

k = int(input("Nhap k: "))

s = s + k
h, m, s = HieuChuan(h, m, s)

print(h, " : ", m , " : ", s)
