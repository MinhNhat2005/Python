# Xử lý ngoại lệ
try:
    print(x)
except:
    print("An exception occurred")
print("----------------------")

# Nhiều ngoại lệ
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Sth else went wrong")
print("----------------------")

# else: trường hợp không có lỗi nào
try:
    print("Hello world")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")
print("----------------------")

# Finally: nếu được chỉ định, sẽ được thực thi bất kể khối try có đưa ra lỗi hay không
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
print("----------------------")

# Cố gắng mở và ghi vào 1 tệp không thể ghi được 
try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close
except:
    print("Something went wrong when opening the file")
print("----------------------")

# Đưa ra 1 ngoại lệ: raise
  # Đưa ra lỗi và dừng chương trình nếu x < 0
x = 1
if x< 0:
    raise Exception("Sorry, no numbers below zero")

x = "Hello"
if not type(x) is int:
    raise TypeError("Only integers are allowed")