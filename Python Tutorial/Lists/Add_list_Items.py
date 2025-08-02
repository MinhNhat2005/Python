# để thêm 1 mục vào cuối danh sách ta dùng append()
list1 = ["apple", "banana", "cherry"]
list1.append("orange")
print(list1)
print("--------------------------------")

# chèn mục (chèn 1 mục vào 1 vị trí mục được chỉ định) insert()
list2 = ["apple", "banana", "cherry"]
list2.insert(2, "chanh")
print(list2)
print("--------------------------------")

# mở rộng danh sách (thêm các phần tử từ danh sách khác vào danh sách hiện tại) extend()
list3 = ["apple", "banana", "cherry"]
list4 = ["táo", "chuối", "dâu"]
list3.extend(list4)
print(list3)
print("--------------------------------")

# thêm bất kỳ Interable nào vào danh sách
list5 = ["apple", "banana", "cherry"]
tuple1 = ("táo", "cam")
dict1 = {"Bưởi", "đào"}
list5.extend(dict1)
list5.extend(tuple1)
print(list5)