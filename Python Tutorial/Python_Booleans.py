print(10>10)
print(10==10)
print(10<9)
print("---------")

a = 200
b = 12
if a>b:
    print("a lớn hơn b")
else:
    print("a < b")

# Đánh giá giá trị và biến

# Đánh giá 1 chuỗi và 1 số
print(bool("Hello"))
print(bool(15))

# Đánh giá 2 biến
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
print("---------")

# Hầu hết các giá trị đều đúng (trừ những giá trị trống)
print(bool("abc"))
print(bool(123))
print(bool(["apple", "banana", "cherry"]))
print("---------")

# Các giá trị trống thì sẽ trả về False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(()))

print("---------")
class myClass():
    def __len__(self):
        return 0
    
myobj = myClass()
print(bool(myobj))
print("---------")

# in ra câu trả lời của 1 hàm 
def myFunction():
    return True

print(myFunction())
print("---------")


# in yes nếu hàm trả về giá trị True còn không thì in No
def myFunction():
    return True

if myFunction():
    print("YES")
else:
    print("NO")
print("---------")

# kiểm tra xem 1 đối tượng có phải làm 1 số nguyên hay không
x = 200
print(isinstance(x, int))