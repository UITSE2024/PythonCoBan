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
            if(bb == 0):
                return NULL
            return aa / bb
        case _:
            return NULL


def main():
    a = int(input("Nhap vao gia tri a: "))
    b = int(input("Nhap vao gia tri b: "))

    kq = xuLy(a, b)

    if(kq != NULL):
        print("Ket qua:", kq)
    else:
        print("Khong hop le")

if __name__ == "__main__":
    main()

