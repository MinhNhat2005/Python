# Tính đa hình
  # Một vd về đa hình có thể sử dụng trên các đối tượng khác nhau là hàm: len()

 # String (Đối với chuỗi tả về số ký tự): len()
x = "Hello World!"
print(len(x))
print("-------------------")

# Tuple (trả về số lượng mục trong tuple): len()
mytuple = ("apple", "banana", "cherry")
print(len(mytuple))
print("-------------------")

# Dict (Đối với dict trả về số cặp key/value): len()
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang", 
    "year" : 2025
}
print(len(thisdict))
print("-------------------")


# Đa hình lớp (các lớp khác nhau với cùng 1 phương thức)
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")
    
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in(car1, boat1, plane1):
    x.move()
print("-------------------")


# Đa hình lớp kế thừa
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("MOVE!")

class Car(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")
    
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()
    print(x.brand)
    print(x.model)
    print("------")
