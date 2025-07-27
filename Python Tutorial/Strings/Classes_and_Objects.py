# Tạo 1 lớp
class MyClass:
    x = 5

# tạo đối tượng
p1  = MyClass()
print(p1.x)
print("-------------------------")

# Tạo 1 lớp Person và sử dụng phương thức __init__() để gán giá trị giống như constructor bên java
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Nhat", 20)
print(p1.name)
print(p1.age)
print(p1)
print("-----------------")


# phương thức __str__(): trả về chuỗi
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.age})"
p1 = Person("John", 36)
print(p1.name)
print(p1)
print("-----------------")


# Tạo phương thức
class Person:
    def __init__(self, name, age, hometown):
        self.name = name
        self.age = age
        self.hometown = hometown

    def myfunc(self):
        print("Hello my name is "+ self.name + f" - I'm {self.age} " + f" - My hometown is {self.hometown}")
p1 = Person("Nhat", 20, "Nghe An")
p1.myfunc()
print("-----------------")

# Tham số bản thân (Sử dụng các từ mysillyobject và abc thay vì selt)
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is "+ abc.name + f"I'm {abc.age}")
p1 = Person("Nhat", 20)
p1.myfunc()
print("-----------------")

#Sửa đổi thuộc tính đối tượng
p1.age = 30
print(p1.age)
p1.myfunc()
print("-----------------")

# Xóa thuộc tính đối tượng: del
del p1.age

# Xóa đối tượng
del p1

# class định nghĩa không thể để trống, nếu không có nội dung thì thêm pass vào để tránh bị lỗi
class Person:
    pass 