import math

def tinhGiaTriHamSo(xx):
    Fx = math.e**xx - xx;
    return Fx;

def main():
    x = float(input("Nhap vao gia tri cua x: "))

    Fx = tinhGiaTriHamSo(x)
    print("Gia tri cua F(x) tai x = {} la {:.2f}".format(x, Fx))

if __name__ == "__main__":
    main()


