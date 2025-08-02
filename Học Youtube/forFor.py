# bài tập in bảng cửu chương 2
for i in range(1,11):
    print("2 x ", i, "=",2*i)

# in ra toàn bộ bảng cửu chương
for i in range(2, 10):
    print("Bảng cửu chương",i)
    for j in range(1, 11):
        print(i,"x", j, "=", i*j)
    print("-----------")  

# vẽ hình chữ nhật
for i in range(1, 6):
    for j in range(1, 11):
        print("* ", end="")
    print()

# vẽ hình tam giác
for i in range(1, 6):         # 5 dòng
    for j in range(1, i+1): # số lượng * trên mỗi dòng tăng dần
        print("*", end="")    # in * trên cùng dòng
    print()                   # xuống dòng sau mỗi hàng

