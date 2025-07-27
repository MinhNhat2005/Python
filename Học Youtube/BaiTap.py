n = -1
while (n<=0):
    n = int(input("Nhập vào n:"))

# chuyển từ thập phân sang nhị phân
ketqua = ""
while (n>0):
    ketqua = ketqua +  str(n%2) 
    print("n%2 = ", n%2)
    n = n//2
    print("n = ", n)
print("ketqua =", ketqua)