# Hàm def()
def myfunc():
    print("Hello Minh Nhật")
myfunc()
print("==================")

# Truyền thông tin vào đối số
def myFunc(fname):
    print(fname + " Refsnes")

myFunc("Emil")
myFunc("Tobias")
myFunc("Linux")
print("==================")

# số lượng đối số phải chính xác
def myfunc(fname, lname):
    print(fname + " " + lname)

myfunc("Phạm", "Nhật")
print("==================")

# Nếu không biết số lượng đối số truyền vào thì dùng * trước tham số
def myfunc(*kids):
    print("The youngest child is "+ kids[2])
myfunc("Emil", 'Tobias', "Linus")
print("==================")

# Đối số với cú pháp key = value
def myfunc(child1, child2, child3):
    print("The younest child is " + child2)
myfunc(child1="Emil",child2= "Tobias",child3= "Linus")
print("==================")

# Nếu không biết số lượng đối số key = value truyền vòa thì dùng ** trước tham số
def myfunc(**kid):
    print("His last name is "+kid["lname"])
myfunc(fname = "Tobias", lname = "Refsnes")
print("==================")


# Giá trị tham số mặc định
def myfunc(country = "Norway"):
    print("I am from "+country)

myfunc("Viet Nam")
myfunc()
myfunc("India")

# Chuyển 1 danh sách làm đối số
def myfunc(food):
    for x in food:
        print(x)
fruits = ['banana', 'cherry', "apple", 12]
myfunc(fruits)
print("==================")

# trả về giá trị: return
def myfunc(x):
    return 5 * x
print(myfunc(3))
print(myfunc(5))
print("==================")

# function không được để trống, nếu không có nội dung thì đưa vào câu lệnh pass để khỏi bị lỗi
def myfunc():
    pass
print("==================")

# Đối số chỉ theo vị trí
def myfunc(x, /):
    print(x)
myfunc(3)
print("==================")

def myfunc(x):
    print(x)
myfunc(x = 3)
print("==================")

# Đối số chỉ từ khóa
def myfunc(*, x):
    print(x)
myfunc(x = 3)
print("==================")

def myfunc(x):
    print(x)
myfunc(3)

# Kết hợp chỉ vị trí và chỉ khóa /,*,
def myfunc(a, b, /, *, c, d):
    print(a+b+c+d)
myfunc(5, 6, c = 7, d= 8)
print("==================")

# Đệ quy
def tri_recursion(k):
    if k>0:
        result = k+ tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result
print("recursion Example Results:")
tri_recursion(6)