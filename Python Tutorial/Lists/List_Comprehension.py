# Hiểu danh sách

# in ra các trái cây có chứa chữ a trong tên
list1 = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in list1 if "a" in x]
print(newlist)
print("--------------------------")

# Cú pháp: newlist = [expression for item in iterable if condition == True]
#(điều kiện chỉ chấp nhận các mục được đánh giá True)
newlist2 = [x for x in list1 if x != "apple"]
print(newlist2)
print("--------------------------")

# không có tuyên bố: if
newlist3 = [x for x in list1]
print(newlist3)
print("--------------------------")

# có thể lặp lại (interable có thể là bất kỳ đối tượng danh sách nào)
newlist4 = [x for x in range(5,10)]
print(newlist4)
print("--------------------------")

# chỉ chấp nhận các số nhỏ hơn 5
newlist5 =[x for x in range(10) if x <=5]
print(newlist5)
print("--------------------------")

# biểu thức đặt các giá trị trong danh sách mới thành chữ hoa
newlist6 = [x.upper() for x in list1]
print(newlist6)
print("--------------------------")

# Đặt tất cả các giá trị trong danh sách mới thành hello
newlist7 = ["hello" for x in list1]
print(newlist7)
print("--------------------------")

# trả về "orange" thay vì "banana"
newlist8 = [x if x != "banana" else "orange"  for x in list1 ]
print(newlist8)