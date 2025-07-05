def Nhap():
    nn = int(input("Nhap n = "))
    return nn

def TinhTong(nn):
    s = 0
    i = 1
    while i <= 2 * nn + 1:
        s = s + 1 / i
        i = i + 2
    return s

def main():
    n = Nhap()
    print("Ket qua:", TinhTong(n))

if __name__ == "__main__":
    main()