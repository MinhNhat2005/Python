# Sắp xếp danh sách

# sắp xếp tăng dùng: sort()
# sắp xếp danh sách theo thứ tự bảng chữ cái
list1 = ["cam", "bưởi", "xoài", "hồng", "quýt"]
list1.sort()
print(list1)
print("-----------------------")

# sắp xếp danh sách theo số
list2 = [30, 3, 123, 3422, 2, 1]
list2.sort()
print(list2)
print("-----------------------")

# Sắp xếp giảm dùng: sort(reverse = True)
list3 = ["orange", "apple", "cherry", "banana", "kiwi"]
list3.sort(reverse=True)
print(list3)
print("-----------------------")

list4 = [12, 234, 13, 2, 2345]
list4.sort(reverse=True)
print(list4)
print("-----------------------")

# Tùy chỉnh chức năng sắp xếp: key = function
# sắp xếp danh sách dự trên mức độ gần với số 50
def myfunc(n):
    return abs(n-50)

list5 = [12, 234, 13, 2, 2345]
list5.sort(key=myfunc)
print(list5)
print("-----------------------")

# sắp xếp phân biệt chữ hoa chữ thường
list5 = ["banana", "Orange", "Kiwi", "cherry"]
list5.sort()
print(list5)
print("-----------------------")

# sắp xếp không phân biệt chữ hoa chữ thường
list6 = ["banana", "Orange", "Kiwi", "cherry"]
list6.sort(key= str.lower)
print(list6)

# Đảo ngược thứ tự: reverse()
list7 = ["banana", "Orange", "Kiwi", "cherry"]
list7.reverse()
print(list7)
