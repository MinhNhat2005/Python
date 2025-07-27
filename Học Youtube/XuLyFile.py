# open
# "x" - tạo file
# r - đọc file
# "a" - nối vào file
# encoding = "utf-8" để tiếng việt không bị lỗi
# file có 2 dạng: + "t" : text
#                   "b" : binary

"""try:  
    f = open("vidu1.txt", "x", encoding="utf-8")
except Exception as e:
    print(e)
"""


try:
    with open("vidu1.py", "a", encoding="utf-8") as f:
        f.write("xin chào các bạn \n")
        f.close
except Exception as e:
    print(e)

# r - đọc file
try:
    with open("vidu1.py", "r", encoding="utf-8") as f:
        noidung = f.read()
        print(noidung)
except Exception as e:
    print(e)

# r - đọc file
try:
    with open("vidu1.py", "r", encoding="utf-8") as f:
        list_noidung = f.readlines()
        i =1
        for noidung in list_noidung:
            print(str(i) + ":" + noidung)
            i+=1
except Exception as e:
    print(e)


# r - đọc file
try:
    with open("vidu1.py", "r", encoding="utf-8") as f:
       noidung = f.readline()
       print(noidung)
except Exception as e:
    print(e)
