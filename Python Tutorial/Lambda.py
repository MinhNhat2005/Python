# Cú pháp             lambda arguments : expression

# Thêm 10 vào đối số và trả về kết quả a
x = lambda a : a+10
print(x(5))
print("-------------------------")

# Hàm lambda có thể nhận bất kỳ số lượng đối số nào
x = lambda a, b : a*b
print(x(5, 6))
print("-------------------------")

x = lambda a, b, c : a+b+c
print(x(5, 6, 7))
print("-------------------------")

def myfunc(n):
    return lambda a: a**n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))