# khởi tạo tuple
# tuple không thể thay đổi(không thể thêm, xóa) và có thể trùng lặp
mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)

# xác định độ dài tuple
mytuple1 = ("apple", "banana", "cherry", "apple", "cherry")
print(len(mytuple1))

# tạo tuple với 1 mục
mytuple2 = ("banana",)
print(type(mytuple2))

# kiểu dữ liệu
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 3, 5,6 ,7)
tuple3 = (True, True, False)
print(type(tuple1))
print(type(tuple2))
print(type(tuple3))

# sử dụng hàm khởi tạo tuple()
tuple4 = tuple(("Minh", "Nhat"))
print(tuple4)

"""
Bộ sưu tập Python
+ List: là một bộ sưu tập được sắp xếp, có thể thay đổi, cho phép các thành viên trùng lặp
+ Tuple: là một bộ sưu tập được sắp xếp, không thể thay đổi, cho phép các thành viên trùng lặp
+ Set: là một bộ sưu tập không theo thứ tự, không thể thay đổi, không có chỉ mục, không được trùng lặp
+ Dictionary: là bộ sưu tập được sắp xếp, có thay đổi, không có trùng lặp
"""