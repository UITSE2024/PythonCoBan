from math import sqrt

def KtNguyenTo(nn):
    if(nn<2):
        return False
    for i in range(2, int(sqrt(nn)) + 1):
        if(nn%i==0):
            return False
    return True

def main():
    n = int(input("Nhap n: "))
    if(KtNguyenTo(n)):
        print("n la so nguyen to")
    else: 
        print("n khong la so nguyen to")

if __name__=="__main__":
    main()