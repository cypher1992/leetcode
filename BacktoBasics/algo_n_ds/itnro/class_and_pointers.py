class Cookie:

    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setColor(self,newColor):
        self.color = newColor


if __name__ == '__main__':
    bc = Cookie("Blue")
    print(bc.getColor())
    bc.setColor("Red")
    print(bc.getColor())

    num1 = 11
    num2 = num1
    print("Num 1", num1)
    print("Num 2", num2)
    print("Num 1 id", id(num1))
    print("Num 2 id", id(num2))
