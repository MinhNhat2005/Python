# cú pháp lambda arguments : expression
# ví dụ vè sử dụng lambda function
kiemTraSoChan = lambda a: (a%2==0)
print(kiemTraSoChan(5))

tinhTong = lambda a, b: a+b
print(tinhTong(5,10))
print(tinhTong(3,2))

# ví dụ về sử dụng lambda function bên trong các function

def hamMu(n):
    return lambda x : x**n

hamMu2 = hamMu(2)
hamMu3 = hamMu(3)

print(hamMu2(3))
print(hamMu3(3))