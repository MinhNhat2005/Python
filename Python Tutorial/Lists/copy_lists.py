# sao chép danh sách: copy()
list1 = ["apple", "banana", "cherry"]
mylist = list1.copy()
print(mylist)
print("--------------------")

# sao chép bằng phương pháp: list()
list2 = ["apple", "banana", "cherry"]
mylist2 = list(list2)
print(mylist2)
print("--------------------")

# sử dụng toán tử lát cắt
list3 = ["apple", "banana", "cherry"]
mylist3 = list3[:]
print(list3)