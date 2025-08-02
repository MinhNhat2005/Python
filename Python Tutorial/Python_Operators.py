"""Python chia các toán tử thành các nhóm sau:

Toán tử số học
Toán tử gán
Toán tử so sánh
Toán tử logic
Toán tử nhận dạng
Nhà điều hành thành viên
Toán tử theo bit
"""
# Toán tử số học 
print(" Toán tử số học ")

x = 5
y = 4
# cộng 
print(x+y)
# trừ
print(x-y)
# nhân 
print(x*y)
# chia
print(x/y)
# chia lấy dư
print(x%y)
# mũ
print(x**y)
# chia lấy phần nguyên 
print(x//y)
print("---------------")

print("Toán tử gán")
# Toán tử gán
x = 5
print("x =",x)
x +=3
print("x =",x)
x -=5
print("x =",x)
x *=4
print("x =",x)
x /=2
print("x =",x)
x %=2
x = 5
print("x =",x)
x //=2
print("x =",x)
x **=3
print("x =",x)
x &= 3
print("x =",x)
x |= 4
print("x =",x)
x ^=3
print("x =",x)
x >>=3
print("x =",x)
x <<=4
print("x =",x)
print(x:=3)
print("---------------")


# Toán tử so sánh
print("Toán tử so sánh")
x = 9
y = 10
print(f"{x}={y}","là",x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)
print("---------------")


# Toán tử logic
# and
x = 5
print(x>3 and x<10)
# or
print(x<5 or x<6)
# not
print(not(x>3 and x< 10))
print("---------------")

# Toán tử nhận dạng
# is
x = ["banana", "cherry"]
y = ["banana", "cherry"]
z = x

print(x is y)
print(x is z)
print(x==y )
# is not
print(x is not y)
print("---------------")

# Toán tử thành viên 
# in 
txt = "Phạm Minh Nhật sinh năm 2005!"
if "Phạm" in txt:
    print("\"Phạm\"có trong txt")
else:
     print("\"Phạm\"khong có trong txt")
print("---------------")

# mức độ ưu tiên toán tử ( dấu ngoặc đơn có độ ưu tiên cao nhất)
print((5+5)-(4+5))
print(100+5*3)
print(5+4-7+3)







