# Xóa các mục

# 1. Xóa mục được chỉ định: remove()
list1 = ["apple", "banana", "cherry"]
list1.remove("banana")
print(list1)
print("------------------------------------")

# 2. Nếu mục được chỉ định có nhiều giá trị trùng lặp thì phương thức này sẽ loại bỏ giá trị đầu tiên
list2 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
list2.remove("apple")
print(list2)
print("------------------------------------")

# 3. Xóa chỉ mục được chỉ định: pop()
list3 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
list3.pop(2)
print(list3)
print("------------------------------------")

# 4. Nếu không đánh chỉ mục thì pop() sẽ xóa phần tử cuối cùng
list4 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
list4.pop()
print(list4)
print("------------------------------------")

# 5. Xóa chỉ mục với từ khóa: del
list5 = ["apple", "banana", "cherry"]
del list5[1]
print(list5)
print("------------------------------------")

# Xóa toàn bộ danh sách (mất luôn)
list6 = ["apple", "banana", "cherry"]
del list6

# Xóa danh sách (làm trống danh sách): clear
list7 = ["apple", "banana", "cherry", "apple", "banana", "cherry"]
list7.clear()
print(list7)
