# Vòng lặp for

# lặp qua 1 chuỗi
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
print("--------------------")

# lặp qua các chữ cái trong từ "banana"
for x in "banana":
    print(x)
print("--------------------")

# break (dừng vòng lặp trong khi vẫn còn đúng)
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    print(x)
    if x == "banana":
        break
print("--------------------")

# Thoát khỏi vòng lặp khi x = "banana" thoát trước khi in banana
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        break
    print(x)
print("--------------------")

# continue (dừng vòng lặp hiện tại và tiếp tục lặp các vòng khác)
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == "banana":
        continue
    print(x)
print("--------------------")

# Hàm range(): trả về 1 dãy số bắt đầu từ 0 theo mặc định và tăng thêm 1 sau mỗi vòng lặp
for x in range(10):
    print(x)
print("--------------------")
# in ra giá trj từ 2 ==> 5
for x in range(2, 10):
    print(x)
print("--------------------")

# Thêm bước nhảy cho hàm range() bằng cách thêm số thứ 3
for x in range(0, 15, 3):  # bước nhảy = 3
    print(x)
print("--------------------")

# thực hiện vòng for và in 1 thông báo khi kết thúc vòng for
for x in range(6):
    print(x)
else:
    print('Finally finished')
print("--------------------")

# khối else sẽ không thực thi nếu vòng lặp bị dừng bởi câu lệnh break
for x in range(6):
    if x == 3: break
    print(x)
else:
    print('Finally finished')
print("--------------------")

# for lồng nhau
# in từng tính từ cho mỗi loại trái cây
adj = ['red', 'big', "tasty"]
fruits = ["apple", "banana", 'cherry']

for x in adj:
    for y in fruits:
        print(x, y)

# for không thể để trống, nếu không có nội dung thì đưa câu lệnh pass để tránh lỗi
for x in [1, 2, 3]:
    pass