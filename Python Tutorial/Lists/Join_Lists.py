# kết nối 2 danh sách
list1 = ["a", "b", "c"]
list2 = [1, 2,4, 5]
list3 = list1 + list2
print(list3)

# cách 2: thêm tất cả các mục từ list2 vào list1
list1 = ["a", "b", "c"]
list2 = [1, 2,4, 5]

for x in list2:
    list1.append(x)
print(list1)

# cách 3: thêm list2 vào cuối list1
list1 = ["a", "b", "c"]
list2 = [1, 2,4, 5]

list1.extend(list2)
print(list1)