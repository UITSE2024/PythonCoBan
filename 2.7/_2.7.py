
s = input("Nhap chuoi s: ")
print("\nChuoi vua nhap la: ", s)
print("\nChuoi dao nguoc la: ")

for i in range(len(s) - 1, -1, -1):
    print(s[i], end = "")