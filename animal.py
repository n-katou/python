class Animal:
    
    # count = 0
    
    def __init__(self, kind, age):
        self.kind = kind
        self.age = str(age) + '歳'
        # Animal.count += 1
        
    def cry(self):
        print('私は' + self.kind + 'です')
    
pochi = Animal("犬", 5)
tama = Animal("猫" , 3)
# print(pochi.kind, pochi.age)
# print(tama.kind, tama.age)
# print(Animal.count)
pochi.cry()
tama.cry()

class Dog(Animal):
    pass
    
    # def run(self):
    #     print('駆け回ります！')

class Cat(Animal):
    
    def __init__(self, kind, age, color):
        super().__init__(kind, age)
        self.color = color
    
    def cry(self):
        print('にゃーん、' + self.kind + 'だにゃん。色は' + self.color + 'だにゃん。')


pochi = Dog('秋田犬', 8)

pochi.cry()
# pochi.run()

tama = Cat('三毛猫', 3,'黒')
tama.cry()




