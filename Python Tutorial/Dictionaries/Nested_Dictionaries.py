# dict lồng nhau
# 1 dict chứa 3 dict
myfamily = {
    "child1": {
        "name" : "Emil",
        "year" : 2004
    },
    "child2":{
        "name": "Tobias", 
        "year": 2007
    }, 
    "child3":{
        "name": "Linus", 
        "year": 2010
    }

}
print(myfamily)
print("============================================")

# Gộp 2 dict vào cùng 1 dict
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
    "child1" : child1, 
    "child2" : child2, 
    "child3" : child3
}
print(myfamily)
print("============================================")


# truy cập các mục trong từ điển lồng nhau
print(myfamily["child2"]["name"])
print(myfamily["child2"]["year"])
print("============================================")

# lặp qua các khóa và giá trị của tất cả các dict lồng nhau
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y+ ":", obj[y])
