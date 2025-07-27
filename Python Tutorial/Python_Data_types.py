# kiểu dữ liệu

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
# kiểu in
x = 5
print(type(x))

# kiểu str
x = "hello"
print(type(x))

# kiểu float
x = 10.0
print(type(x))

# kiểu complex
x = 1j
print(type(x))

# kiểu list
x = ["hello", "Minh", "Nhat"]
print(type(x))

# kiểu tuple
x = ("hello","Minh","Nhat")
print(type(x))

# kiểu range
x = range(5)
print(type(x))

# kiểu dict
x = {"ten":"Nhat", "tuoi": 20}
print(type(x))

# kiểu set
x = {"hello", "Minh","Nhat"}
print(type(x))

# kiểu frozenset
x = frozenset({"hello", "Minh","Nhat"})
print(type(x))

# kiểu bool
x = True
print(type(x))

# kiểu bytes
x = b"hello"
print(type(x))

# kiểu bytearray
x = bytearray(5)
print(type(x))

# kiểu memoryview
x = memoryview(bytes(5))
print(type(x))

# kiểu noneType
x = None
print(type(x))

# ép kiểu dữ liệu thì thêm từ khóa của kiểu dữ liệu muốn ép trước biến là được 
x = 5  # kiểu in
print(type(x))
x = str(5) #kiểu str
print(type(x))

# có thể khoai báo tên kiểu dữ liệu trước values
x = float(20)
print(type(x))