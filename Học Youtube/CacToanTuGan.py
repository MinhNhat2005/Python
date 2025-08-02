print("Tất cả các phép gán trong Python:")

# Phép gán cơ bản
a = float(input("Nhập vào a:")) 
print("a =", a)

# Phép gán cộng
a += 5  # tương đương a = a + 5
print("a += 5 =>", a)

# Phép gán trừ
a -= 3  # tương đương a = a - 3
print("a -= 3 =>", a)

# Phép gán nhân
a *= 2  # tương đương a = a * 2
print("a *= 2 =>", a)

# Phép gán chia
a /= 4  # tương đương a = a / 4
print("a /= 4 =>", a)

# Phép gán chia lấy nguyên
a //= 2  # tương đương a = a // 2
print("a //= 2 =>", a)

# Phép gán chia lấy dư
a %= 3  # tương đương a = a % 3
print("a %= 3 =>", a)

# Phép gán lũy thừa
a **= 4  # tương đương a = a ** 4
print("a **= 4 =>", a)

# Đặt lại giá trị để thử với các phép bit
a = 5
print("\nThử với phép bit:")

# Phép gán AND bit
a &= 3  # tương đương a = a & 3
print("a &= 3 =>", a)

# Phép gán OR bit
a |= 2  # tương đương a = a | 2
print("a |= 2 =>", a)

# Phép gán XOR bit
a ^= 1  # tương đương a = a ^ 1
print("a ^= 1 =>", a)

# Phép gán dịch trái
a <<= 1  # tương đương a = a << 1
print("a <<= 1 =>", a)

# Phép gán dịch phải
a >>= 2  # tương đương a = a >> 2
print("a >>= 2 =>", a)
