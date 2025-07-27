# Tạo danh sách
list1 = ["apple","banana","cherry"]
print(list1)
print("------------------")

# Danh sách cho phép trùng lặp
list1 = ["apple","banana","cherry", "apple","cherry"]
print(list1)
print("------------------")

# Độ dài danh sách (in số lượng mục trong danh sách)
list1 = ["apple","banana","cherry"]
print(len(list1))
print("------------------")

# Mục danh sách - kiểu dữ liệu
# các mục danh sách có thể thuộc bất kỳ loại dữ liệu nào
list1 = ["apple", "banana", "cherry"]
list2 = [1, 4, 2, 6, 7]
list3 = [True, False, True]
print(list1, type(list1))
print(list2, type(list2))
print(list3, type(list3))
print("------------------")

# Một danh sách có thể chứa các loại dữ liệu khác nhau
list4 = [1, "Nhat", True, 10.4]
print(list4)
print("------------------")

# kiểu dữ liệu
print(type(list4))
print("------------------")

# Hàm tạo list (Cũng có thể sử dụng hàm khởi tạo để tạo 1 list: list())
list5 = list(("Phạm","Minh","Nhật"))
print(list5)
