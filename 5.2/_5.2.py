def Nhap(nn):
    students = []

    for i in range(nn):
        print("Sinh vien {}".format(i + 1))
        maSV = input("Nhap vao ma sinh vien: ")
        tenSV = input("Nhap vao ten sinh vien: ")
        Lop = input("Nhap vao lop sinh vien: ")

        student = {
            "maSV": maSV,
            "tenSV": tenSV,
            "Lop": Lop
        }

        students.append(student)

    return students 


def Xuat(students):
    print("\nXuat danh sach:\n")
    for student in students:
        print(student)

def main():
    n = int(input("Nhap vao n: "))

    students = Nhap(n)
    Xuat(students)

if __name__ == "__main__":
    main()

