# Xóa mục 
# Để xóa mục trong set, dùng remove() hoặc discard()
set1 = {"banana", "apple", "cherry"}
set1.remove("banana")
print(set1)
set1.discard("cherry")
print(set1)

# Xóa ngẫu nhiên bằng phương thức: pop()
set2 = {"banana", "apple", "cherry"}
set2.pop()
print(set2)


# Dọn sách set bằng phương thức: clear()
set3 = {"banana", "apple", "cherry"}
set3.clear()
print(set3)


# Xóa hoàn toàn tập hợp: del
set4 = {"banana", "apple", "cherry"}
del set4

# copy set
x = set2.copy()
print(x)