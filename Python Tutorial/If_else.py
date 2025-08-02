# if
a = 23
b = 200
if b>a:
    print("b > a")
print("------------------")

# elif
a = 33
b = 33
if b>a:
    print("b>a")
elif a==b:
    print("a = b")
print("------------------")

# else
a = 200
b = 33
if b>a:
    print("b>a")
elif a==b:
    print(a=b)
else:
    print("a > b")
print("------------------")

# if else
a = 200
b = 33
if b>a:
    print("b > a")
else:
    print("b < a")
print("------------------")


# thực thi trên cùng 1 dòng
if a>b: print("a > b")
print("------------------")


# Viết if và else trên cùng 1 hàng
a = 3
b = 22
print("A") if a>b else print("B")
print("------------------")


# Nhiều if else trên cùng 1 dòng
a = 22
b = 343
print("A") if a>b else print("=") if a==b else print("B")
print("------------------")

# Từ khóa and sử dụng để kết hợp điều kiện
a = 200
b = 33
c = 440
if a>b and c>a:
    print("Các điều kiện đều đúng")
print("------------------")

# Từ khóa or 
a = 4
b = 3
c = 2
if a>b  or c>a:
    print("Ít nhất 1 trong các điều kiện là đúng")
print("------------------")

# Từ khoá not(đảo ngược kết quả của câu lệnh điều kiện)
a = 33
b = 200
if not a>b:
    print("b > a")
print("------------------")

# if lồng nhau
x = 54
if x>10:
    print("Above ten")
    if x > 20:
        print("and alse above 20!")
    else:
        print("but not above 20")
print("------------------")

# if không được để trống, để tránh lỗi thì nên để pass
a = 33
b = 200
if b>a:
    pass