import sqlite3

# tạo kết nối với csdl
conn = sqlite3.connect('D:/python.db')
cursor = conn.cursor()
print("kết nối dữ liệu thành công")

# tạo table
cursor.execute("""
CREATE TABLE IF NOT EXISTS monhoc(
     mamh   TEXT PRIMARY KEY,
     tenmh  TEXT NOT NULL,
     sotinchi INTERGER NOT NULL CHECK (sotinchi > 0)             
               );
""")
conn.commit()
print("Đã tạo xong bảng monhoc")

# thêm dữ liệu vào table monhoc
monhoc_Data = [
    ("TRR", "Toán rời rạc", "3"),
    ("XSTK", "Xác suất thống kê", "2"), 
    ("LTDD", "Lập trình di động", "3"),
    ("CNPM", "Công Nghệ phần mềm", "2")
]
# cursor.executemany("INSERT INTO monhoc(mamh, tenmh, sotinchi) VALUES (?,?,? )", monhoc_Data)
conn.commit()
print("Đã thêm dữ liệu vào bảng monhoc")

# lấy tất cả dữ liệu từ bảng monhoc
cursor.execute("SELECT * FROM monhoc")
danhSach = cursor.fetchall()
for row in danhSach:
    print(row)


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


# tạo table diemthi
cursor.execute("""
CREATE TABLE IF NOT EXISTS diemthi(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        masv TEXT NOT NULL,
        mamh TEXT NOT NULL,
        diem REAL CHECK (diem BETWEEN 0 AND 10), 

        -- Ràng buộc khóa ngoại:
        FOREIGN KEY (masv) REFERENCES sinhvien(masv)
               ON UPDATE CASCADE
               ON DELETE CASCADE,
        FOREIGN KEY (mamh) REFERENCES monhoc(mamh), 
        UNIQUE(masv, mamh)  
                    
               )
""")
conn.commit()
print("Đã tạo xong bảng điểm thi")

# thêm dữ liệu vào table diemthi
diemthi_data = [
       ("23IT.B152", "TRR", 10), 
       ("23IT273", "LTDD", 8), 
       ("123", "CNPM", 10)
]
try:
    cursor.executemany("INSERT INTO diemthi (masv, mamh, diem) VALUES (?, ?, ?)", diemthi_data)
    conn.commit()
    print("Đã thêm dữ liệu vào bảng diemthi thành công.")
except sqlite3.IntegrityError as e:
    print("Lỗi khi thêm dữ liệu:", e)


conn.close()