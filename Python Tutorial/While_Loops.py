# Vòng lặp while

# in ra i với i <= 10
i = 1
while i <= 10:
    print(i)
    i+=1
print("--------------------------")


# break
# dừng vòng lặp thi i = 3
i = 0
while i <5:
    print(i)
    if i ==3:
        break
    i+=1
print("--------------------------")

# continue (Dừng lặp hiện tại và tiếp tục lặp với lần lặp tiếp theo)
i = 0
while i <5:
    i +=1
    if i ==3:  # i = 3 thì không in ra còn lại in ra các giá trị khác 
        continue
    print(i)
print("--------------------------")

# else ( thực hiện một khối mã một lần khi đk không còn đúng)
i = 0
while i < 10:
    print(i)
    i +=1
else:
    print("i không lớn hơn 9")
