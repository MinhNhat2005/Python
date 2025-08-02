try:
    a = int(input("Nhập vào số nguyên a: "))
    print(a + 5)
except:
    print("Nhập dữ liệu không chính xác") 


try:
    a = int(input("Nhập vào số nguyên a: "))
    print(a + 5)
except Exception as e:
    print(e) 
else:
    print("Không có lỗi xảy ra!")
finally:
    print("Kết thúc chương trình!")
