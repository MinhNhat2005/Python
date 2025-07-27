# Bộ lặp: iter()

# Trả về một bộ lặp từ 1 bộ và in từng giá trị
mytuple = ("apple", "banana", 'cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print("----------------------")

# Chuỗi cũng là đối tượng có thể lặp lại 
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("----------------------")

# Bộ lặp: for
mytuple = ("Banana", "apple", "cherry")
for x in mytuple:
    print(x)
print("----------------------")

# Lặp lại các ký tự chuỗi
mystr = "banana"
for x in mystr:
    print(x)
print("----------------------")

# Tạo một trình lặp lại
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x
    
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))
print(next(myclass))
print("----------------------")

# Dừng lặp lại
# Dừng sau 20 lần lặp 
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
        
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)