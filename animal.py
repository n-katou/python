class Animal:
    
    count = 0
    
    def __init__(self, kind, age):
        self.kind = kind
        self.age = str(age) + '歳'
        Animal.count += 1
        
    def cry(self):
        print('私は' + self.kind + 'です')
    
pochi = Animal("犬", 5)
tama = Animal("猫" , 3)
# print(pochi.kind, pochi.age)
# print(tama.kind, tama.age)
# print(Animal.count)
pochi.cry()
tama.cry()