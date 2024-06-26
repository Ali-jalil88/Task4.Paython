class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"{self.name} {self.age}")
    def sit (self):
        print("dog is sit")
    def roll_over(self):
        print("Dog is Hier")
dog=Dog("Hisky",20)
dog.sit()
dog.roll_over()
        
        
