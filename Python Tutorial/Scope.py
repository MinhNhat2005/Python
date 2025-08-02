# Phạm vi trong Python

# Phạm vi toàn cục
def myfunc():
    x = 300
    print(x)

myfunc()  # In ra 300
print("----------------")

# truy cập từ hàm trong hàm
def myfunc2():
   x = 300
   def myinnerfunc():
       print(x)
   myinnerfunc()
myfunc()
print("----------------")

# Phạm vi toàn cầu (Một biến được tạo bên ngoài 1 hàm là toàn cục và có thể được sử dụng bất cứ đâu)
x = 300
def myfunc():
    print(x)
myfunc()
print("----------------")

# Nếu biến trong hàm và biến ngoài hàm cùng tên thì nó vẫn hoạt động 2 biến độc lặp
x = 10
def myfunc():
    x = 14
    print(x)
myfunc()  # in x trong hàm

print(x)  # in x cục bộ
print("----------------")

# Từ khóa toàn cầu: Global
def myfunc():
    global x
    x = 20
myfunc()
print(x)
print("----------------")

# thay đổi giá trị của 1 biến toàn cục bên trong hàm
x = 12

def myfunc():
    global x 
    x = 50

myfunc()
print(x)
print("----------------")

# các hàm lồng nhau sử dụng nonlocal để làm cho biến thuộc về hàm bên ngoài
def myfunc1():
    x = "Jae"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return(x)
print(myfunc1())