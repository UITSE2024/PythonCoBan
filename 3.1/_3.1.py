x = input("So thu nhat: ")
y = input("So thu hai: ")
z = input("So thu ba: ")
x, y, z = map(int, (x, y, z))

if y < x:
    x = y
if z < x:
    x = z

print(x)