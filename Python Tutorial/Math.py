# Toán

# Tìm giá trị lớp nhất trong iterable
x = max(5, 10, 25)
print("max = ",x)
print("--------------")

# Tìm giá trị nhỏ nhất trong iterable
y = min(12, 2, 34)
print("min = ",y)
print("--------------")

# Hàm trả feef giá trị tuyệt đối: abs()
x = abs(-7.25)
print("|x| = ",x)
print("--------------")

# Hàm trả về hàm mũ
x = pow(4, 3)
print("4^3 = ",x)
print("--------------")

# mô đun toán học
import math
# trả về căn bậc 2
x = math.sqrt(64)
print("Căn bậc 2 =", x)
print("--------------")

# làm tròn 1 số lên số nguyên gần nó nhất và làm tròn số xuống số nguyên gần nó nhất
x = math.ceil(1.4)
y = math.floor(1.4)

print(x)  # return 2
print(y)  # return 1
print("--------------")

# hằng số (trả về giá trị của PI)
x = math.pi
print("PI =",x)