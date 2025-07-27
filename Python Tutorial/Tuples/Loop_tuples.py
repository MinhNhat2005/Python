# vòng lặp 

# lặp qua các mục và in các giá trị 
tuple1 = ("apple", "banana", "cherry")
for x in tuple1:
    print(x)
print("--------------")

# lặp qua các chỉ số mục
tuple2 = ("apple", "banana", "cherry")
for i in range(len(tuple2)):
    print(tuple2[i])
print("--------------")

# Sử dụng vòng lặp while
tuple3 = ("apple", "banana", "cherry")
i = 0
while i < len(tuple3):
    print(tuple3[i])
    i +=1