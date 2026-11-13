class Dog:
    rabid=False
    weight=0
    name="abc"
    def growl(self):
        print(f"{self.name} says grr")
    def eat(self, food):
        self.weight += food
        print(f"{self.name} now weighs {self.weight}")

d1=Dog()
d1.name="Alice"
print("D1 Name =",d1.name)
print("D1 Weight =",d1.weight)

Dog.name="xyz"
Dog.weight=500

print("D1 Name =",d1.name)
print("D1 Weight =",d1.weight)