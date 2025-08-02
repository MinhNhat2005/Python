# tạo 1 lớp có tên MyClass
class MyClass:
    x = 5

# tạo đối tượng
p1 = MyClass()
print(p1.x)

# tạo lớp với hàm __init__()
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Nhat", 20)

print(p1.name)
print(p1.age)
print(p1)

# tạo lớp với hàm __str__()
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}{self.age}"

p1 = Person("John", 36)

print(p1)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name + " I'm " + str(self.age) + " year old")

p1 = Person("John", 36)
p1.myfunc()