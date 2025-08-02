# bài tập về động vật
# xây dựng class cha
class Animal:
    # constructor: xây dựng ra đối tượng
    def __init__(self, animalTypeA, nameA, widthA, heightA, weightA):
        self.animalType = animalTypeA
        self.name = nameA
        self.width = widthA
        self.height = heightA
        self.weight = weightA

    # phát âm thanh
    def makeVoice(self):
        print("Unknow voice")

    # in thông tin 
    def printMe(self):
        print("animalType={0}, name={1}, width={2}, height={3}, weight={4}".format(self.animalType, self.name, self.width, self.height, self.weight))

        
a1 = Animal("con người", "NGuyễn Văn A", "", "170cm", "60kg")
a1.printMe()
a1.makeVoice()

class Dog(Animal):
    # constructor của lớp con:
    def __init__(self, nameA, widthA, heightA, weightA, isChampionA):
        # gọi constructor của lớp cha
        Animal.__init__(self, "Dog", nameA, widthA, heightA, weightA)
        # gán giá trị cho các thuộc tính bổ sung
        self.isChampion = isChampionA

    # override method
    def makeVoice(self):
        print("{0}: gau gau".format(self.name))

dog1 = Dog("Cậu vàng","80cm", "40cm","20kg", True)
dog2 = Dog("Mật", "850cm", "100cm", "50kg", True)
dog1.makeVoice()
dog1.printMe()
dog2.makeVoice()
dog2.printMe()


class Cat(Animal):
    # constructor lop con
    def __init__(self, nameA, widthA, heightA,weightA, colorA):
        # goi constructor lop cha
        Animal.__init__(self, "Cat", nameA, widthA, heightA, weightA)
        # gán giá trị cho các thuộc tính bổ sung
        self.color = colorA

     # override methoed
    def makeVoice(self):
        print("{0} meo meo".format(self.name))

meo1 = Cat("mèo con", "30cm", "15cm","5kg", "vàng")
meo1.printMe()
meo1.makeVoice()    

        