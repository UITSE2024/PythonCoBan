se_address = input("Nhap dia chi se: ")

vt1 = se_address.find("@")
vt2 = se_address.find(".")

if vt1 < 0 or vt2 < 0:
    print("Dia chi se khong hop le!")
else:
    x = se_address[:vt1]
    y = se_address[(vt1 + 1):vt2]
    z = se_address[(vt2 + 1):]
    if x == "" or y == "" or z == "":
        print("Dia chi se khong hop le!")
    else:
        print("Dia chi se hop le!")
