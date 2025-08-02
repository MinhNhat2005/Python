# câu lệnh break (dừng lại)
for i in range(0, 10):
    print(i)
    if i>5:
        break

n = 100
while(n>0):
    print(n)
    n=n//2
    if n<50:
        break

# câu lệnh continue (bỏ qua)
for i in range(0, 10):
    if i%2==1:
        continue
    else:
        print(i)

