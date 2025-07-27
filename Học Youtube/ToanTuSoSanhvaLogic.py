x = float(input("Nhập vào x: "))
y = float(input("Nhập vào y: "))

# các toán tử so sánh
print("x < y là :", x<y)
print("{0}<{1} là {2}".format(x, y, x<y))
print("{0}>{1} là {2}".format(x, y, x>y))
print("{0}>={1} là {2}".format(x, y, x>=y))
print("{0}<={1} là {2}".format(x, y, x<=y))
print("{0}=={1} là {2}".format(x, y, x==y))
print("{0}!={1} là {2}".format(x, y, x!=y))

# các toán tử logic
z = float(input("Nhập vào z:"))
print(x<y and y <z)
print(x<y or y<z)
print(not(x<z))