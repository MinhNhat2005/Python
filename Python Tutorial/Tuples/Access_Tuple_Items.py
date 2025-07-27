# Truy cập các mục tuple

tuple1 = ("apple", "banana", "cherry")
print(tuple1[1])
print("------------------------------")

# lập chỉ mục tiêu cực (mục cuối cùng là -1 và giảm giần về phía đầu)
tuple2 = ("apple", "banana", "cherry")
print(tuple2[-1])
print(tuple2[-2])
print("------------------------------")

# phạm vi chỉ số
tuple3 = ("apple", "banana", "cherry", "grape", "orange")
print(tuple3[2:5])
print("------------------------------")

# phạm vi bắt lấy khoảng đầu
tuple4 = ("apple", "banana", "cherry", "grape", "orange")
print(tuple4[:3])
print("------------------------------")

# phạm vi lấy khoảng cuối
tuple5 = ("apple", "banana", "cherry", "grape", "orange")
print(tuple5[3:])
print("------------------------------")

# Phạm vi các chỉ số tiêu cực
tuple6 = ("apple", "banana", "cherry", "grape", "orange")
print(tuple6[-5:-3])
print("------------------------------")

# kiểm tra phần tử có tồn tại trong tuple không
tuple7 = ("apple", "banana", "cherry", "grape", "orange")
print("Yes") if "apple" in tuple7 else "No"