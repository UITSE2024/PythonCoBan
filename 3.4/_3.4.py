from zmq import NULL


def xuLy(aa, bb):
    ch = input("Nhap vao 1 phep toan(+ - * /): ")

    match ch:
        case '+':
            return aa + bb 
        case '-':
            return aa - bb
        case '*':
            return aa * bb
        case '/':
            if(b == 0):
                return NULL
            return aa / bb
        case _:
            print("Toan tu khong hop le")
            return NULL


def main():
    a = int(input("Nhap vao gia tri a: "))
    b = int(input("Nhap vao gia tri b: "))

    kq = xuLy(a, b)

    print("Ket qua:", kq)

if __name__ == "__main__":
    main()

