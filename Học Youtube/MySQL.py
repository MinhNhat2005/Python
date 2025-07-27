import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    password = "",
    database = "minhnhat"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM sinhvien")
rows = cursor.fetchall()
for row in rows:
    print(row)

# thêm dữ liệu vào table
sinhvien_data = [
    ("23IT.B152", "Phạm Minh Nhật", "10"),
    ("23IT273", "Nguyễn Thị Thùy Tiến", "9"),
    ("23IT001", "Hò Văn Tẻn", "8")
]
# cursor.executemany("INSERT INTO sinhvien(masv, hovaten, diemtb) VALUES (%s,%s,%s)", sinhvien_data)
conn.commit()
print("Đã thêm dữ liệu thành công!")

# show database
cursor.execute("SHOW DATABASES")
for x in cursor:
    print(x)



conn.close()