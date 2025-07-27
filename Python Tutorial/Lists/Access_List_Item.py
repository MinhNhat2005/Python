# Truy cập chỉ mục (mục đầu tiên từ trái sang có chỉ mục là 0)
list1 = ["apple","banana","cherry"]
print(list1[1])
print("-------------")

# Truy cập chỉ mục (âm) mục cuối cùng có chỉ mục là -1
list2 = ["apple","banana","cherry"]
print(list2[-1])
print("-------------")

# phạm vi chỉ số (lấy trong 1 khoảng)
list3 = ["apple","banana","cherry","grape","melon","orange"]
print(list3[2:5])
print("-------------")

# lấy khoảng từ đầu đến 1 chỉ mục bất kỳ (nhưng không bao gồm mục đó)
list4 = ["apple","banana","cherry","grape","melon","orange"]
print(list4[:4])
print("-------------")


# lấy khoảng từ chỉ mục bất kỳ đến cuối cùng
list5 = ["apple","banana","cherry","grape","melon","orange"]
print(list5[4:])
print("-------------")

# phạm vi chỉ số tiêu cực (lấy trong 1 khoảng)
list6 = ["apple","banana","cherry","grape","melon","orange"]
print(list6[-4:-1])
print("-------------")

# kiểm tra xem có tồn tại không
list7 = ["apple","banana","cherry","grape","melon","orange"]
if "melon" in list7:
    print("YES, melon in the fruits list!")
else:
    print("No")