# biến toàn cục

x = "awesome"
def myFunc():
    print("Python is "+x)
myFunc()
print("-------------------")

# tạo biến trong hàm với trên trùng với tên biến toàn cục
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is "+x)
myfunc()

print("Python is"+x)

print("-------------------")

# sử dụng từ khóa global
def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is "+x)

print("-------------------")

# thay đổi 1 biến toàn cục bên trong 1 hàm
x = "Đẹp"
def ten():
    global x
    x = "Đẹp trai"

ten()
print("Phạm Minh Nhật "+x)


x = {"name" : "John", "age" : 36}
print(type(x))