n = int(input("Nhap n = "))

c = 0
s = 0
t = n

while t != 0:
    dv = t % 10
    s = s + dv
    c = c + 1
    t = t // 10

print("So chu so:", c)
print("Tong cac chu so:", s)