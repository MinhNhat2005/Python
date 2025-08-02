# Xóa file (để xóa 1 file thì phải nhập module hệ điều hành và chạy chức năng os.remove())
# Xóa file demofile.py

import os
os.remove("demofile.py")



# Kiểm tra xem file có tồn tại hay không
import os 
if os.path.exists("test.py"):
    os.remove("test.py")
else:
    print("The file does not exits")

# Xóa thư mục
import os 
os.rmdir("myfolder")