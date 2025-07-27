# thêm mục: add()
set1 = {"apple", "banana", "cherry"}
set1.add("kiwi")
print(set1)

# Thêm set: update()
set2 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
set2.update(tropical)
print(set2)

# thêm bất kỳ Iterable nào
set3 = {"apple", "banana", "cherry"}
list1 = ["kiwi", "orange"]
set3.update(list1)
print(set3)