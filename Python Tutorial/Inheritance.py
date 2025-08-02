# Tạo lớp cha
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

p1 = Person("John", "Doe")
p1.printname()
print("==============================================")

# Tạo lớp con kết thừa từ lớp cha
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()
print("==============================================")

# Thêm hàm __init__() thay vì từ khóa pass
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("welcome", self.fname, self.lname, "To the FPT company of ", self.graduationyear)
x = Student("Pham", "Nhat", 2027)
x.welcome()