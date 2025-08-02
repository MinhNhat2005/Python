# yêu cầu người dùng nhập vào số lớn hơn 0 nếu nhập sai thì nhập lại
n = -1
while (n<=0):
    n = float(input("Nhập vào n:"))

# tính tổng từ 0 đến n
i = 0
tong = 0
while (i<=n):
    tong+=i
    i+=1
print(tong)

# in ra các giá trị của j
j = 0
while (j<=10):
    j+=1
    print(j) 
  
else:
    print(j,"Bên ngoài vòng lặp!")
    
