# kết nối CSDL

# import thư viện
import sqlite3

# kết nối đến cơ sở dữ liệu
conn = sqlite3.connect('D:/python.db')
cursor = conn.cursor()

# Lấy danh sách tất cả các bảng
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("📋 Tất cả dữ liệu trong CSDL:\n")

# Duyệt từng bảng và lấy dữ liệu
for table in tables:
        table_name = table[0]
        print(f"-----bảng : {table_name}-----")
        
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if rows:
                for row in rows:
                        print(row)
        else:
                print("không có dữ liệu")

print("\n Hoàn tất")

# thêm dữ liệu vào bảng
"""cursor.execute("INSERT INTO sinhvien(masv, hovaten, diemtb) VALUES (?,?,?)", ("125", "NGUYEN THI B", "5"))
conn.commit()"""

# sửa dữ liệu 
cursor.execute("UPDATE sinhvien SET diemtb = ? WHERE masv = ? ", (10, "123"))
conn.commit()
print("✅ Đã cập nhật thành công.")

# xóa dữ liệu
cursor.execute("DELETE FROM sinhvien WHERE masv = '121'")
conn.commit()
print("Đã xóa thành công")

# lấy dữ liệu từ bảng sinhvien
cursor.execute("SELECT * FROM sinhvien WHERE sinhvien.diemtb = ?", (5,))
danhSach = cursor.fetchall()
for row in danhSach:
        print(row)

# in masv từ bé đến lớn
cursor.execute("SELECT * FROM sinhvien ORDER BY masv ASC")
result = cursor.fetchall()
for row in result:
        print(row)



