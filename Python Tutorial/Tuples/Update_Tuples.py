# Chuyển đổi tuple thành list để thay đổi nó và chuyển về lại tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
print("----------------------")

# thêm mục
y.append("Chuối")
x = list(y)
print(x)

# Thêm 1 tuple vào 1 tuple
z = ("Bưởi", "đào")
x += z
x = tuple(x)
print(x)

# Xóa phần tử 
y = list(x)
y.pop(4)
x = tuple(y)
print(x)
del x
