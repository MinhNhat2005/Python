# Nối 2 set dùng: union() hoặc |
set1 = {"a", "b", "c"}
set2 = {1,3,4}
set4 = {True, False}
set6 = {"Phạm", "Minh", "Nhật"}
set3 = set1.union(set2)
set5 = set1 | set4
print(set3)
print(set5)
print("1---------------------------")
 
# Nối nhiều tập hợp bằng phương pháp: union()
myset = set1.union(set2, set4, set6)
print(myset)
print("2---------------------------")
# dùng |
MySet = set1 | set2 | set4 |set6
print(MySet)
print("3---------------------------")

# Nối 1 set với các kiểu dữ liệu khác
x = {"a", "b", "c"}
y = (1, 2,4, 5)
t = [True, False, False]
z = x.union(y, t)
print(z)
print("4---------------------------")


# CẬP NHẬT (phương pháp chèn tất cả các mục từ tập hợp này vào tập hợp khác)
set1 = {"a", "b", "c", 3}
set2 = {1,2,3}
set1.update(set2)
print(set1)
print("5---------------------------")

# intersection() hoặc &: phương pháp này trả về 1 tập hợp mới chỉ chưa các mục có cả trong 2 set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)
set4 = set1 & set2
print(set4)
print("6---------------------------")

# intersectione_update(): Giữ lại các mục tồn tại trong cả set1 và set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
print("7---------------------------")

# Nối các set chứa các giá trị được xem là trùng lặp: True-1, False-0
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {"google", False, 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3)
print("8---------------------------")

# Sự khác nhau: 
# difference hoặc - : Giữ lại tất cả các mục có trong set1 mà không có trong set2
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)
print(set3)
print("9---------------------------")
# -
set4 = {"a", "b", "c"}
set5 = {1, 2, "a"}
set6 = set4 - set5
print(set6)
print("10---------------------------")

# difference_update(): giữ các mục ở bộ đầu tiên không có trong bộ thứ 2 
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)
print("11---------------------------")

# sự khác biệt đối xứng
# phương pháp này sẽ giữ lại các phần tử không có trong cả 2 tập hợp: symetric_difference() hoặc ^
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
print("12---------------------------")

# Phương pháp giữ lại các mục không có trong cả 2 bộ: symetric_difference_update()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)

