# Danh sách vòng lặp

# lặp lại qua 1 danh sách: for
# in tất cả danh sách, từng mục 1
list1 = ["banana", "apple", "cherry"]
for x in list1:
    print(x)
print("------------------------")

# lặp qua các chỉ số mục
list2 = ["banana", "apple", "cherry"]
for i in range(len(list2)):
    print(list2[i])
print("------------------------")

# sử dụng vòng lặp while
list3 = ["banana", "apple", "cherry"]
i = 0
while i < len(list3):
    print(list3[i])
    i +=1
print("------------------------")

# lặp lại bằng cách sử dụng cách hiểu danh sách
list4 = ["banana", "apple", "cherry"]
[print(x) for x in list4]