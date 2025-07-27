# set không có thứ tự, không thể thay đổi, không có giá trị trùng lặp
set1 = {"apple", "banana", "cherry"}
print(set1)

# Các giá trị trùng lặp sẽ bị bỏ qua và chỉ lấy 1 giá trị
set2 = {"apple", "banana", "apple", "strawberry"}
print(set2)

# True và 1 được coi là cùng giá trị
set3 = {1, 3, "nho", True}
print(set3)

# False và 0 được coi là cùng 1 giá trị
set4 = {False, 1, 0, "banana"}
print(set4)

# Độ dài của 1 set
# set5 có len = 6 vì True và 1 là 1 giá trị , False và 0 là 1 giá trị
set5 = {"banana", 1, True, False, 0, 3, 5, "apple"}
print(len(set5))

# set có thể chứa bất kỳ kiểu dữ liệu nào
set6 = {"apple", "banana"}
set7 = {1,2, 5,6}
set8 = {True, False }
print(type(set6))

# 1 set có thể chứa nhiều kiểu dữ liệu
set9 = {"banana", 1, 5, True, "male"}
print(set9)

# Hàm tạo set()
set10 = set(("apple", "banana", "cherry"))
print(type(set10))