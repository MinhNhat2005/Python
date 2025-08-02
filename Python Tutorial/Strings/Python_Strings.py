# String trong python có thể dùng dấu nháy đơn hoặc dấu nháy kép
print("Hello")
print('Hello')

# có thể dùng dấu nháy trong chuỗi miễn là không trùng với dấu nháy 2 đầu chuỗi
print("It's a alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a, type(a))

a = """Phạm Minh Nhật, 
  Sinh năm 2005,
       tại Nam Kim Nam Đàn Nghệ An
       Học giỏi.

"""
print(a, type(a))

a = '''Phạm Minh Nhật, 
  Sinh năm 2005,
       tại Nam Kim Nam Đàn Nghệ An
       Học giỏi.

'''
print(a, type(a))

x = "Hello, World"
print(x[5])
print(len(x))

# lặp qua 1 chuỗi
for x in "Banana":
    print(x)

# kiểm tra chuỗi
txt = "The best things in life are free!"
print("in" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")

txt = "The best things in life are free!"
print("nhat" not in txt)

txt = "The best things in life are free!"
if "nhat" not in txt:
    print("No, 'nhat' is not present")