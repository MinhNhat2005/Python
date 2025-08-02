# Thay đổi giá trị mục
list1 = ["apple", "banana", "cherry"]
list1[1] = "blackcurrant"
print(list1)
print("--------------------------------------")

# thay đổi phạm vi giá trị mục
list2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list2[1:3] = ["blackrrant", "watermelon"]
print(list2)
print("--------------------------------------")

# thay đổi 1 giá trị bằng cách chèn nhiều giá trị hơn vào
list3 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
list3[1:2] = ["chanh", "cam", "nho"]
print(list3)
print("--------------------------------------")

# thay thế nhiều giá trị bằng cách chèn vào 1 giá trị
list4 = ["apple", "banana", "cherry"]
list4[1:3] = ["chanh"]
print(list4)

# Chèn mục (không làm thay đổi giá trị hiện có): insert()
# chèn mận vào sau chanh có chỉ mục là 2 
list5 = ["táo", "chanh", "ổi", "hồng"]
list5.insert(2, "mận")
print(list5)