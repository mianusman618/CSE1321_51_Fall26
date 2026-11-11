class Dog:
    rabid=False
    weight=0
    name=""
    def growl(self):
        print(f"{self.name} says grr")
    def eat(self, food):
        self.weight += food
        print(f"{self.name} now weighs {self.weight}")
d1 = Dog()
d1.name = "Alice"
d1.rabid = True
d1.weight = 50.0

d2 = Dog()
d2.name = "Bob"
d2.weight = 30.0

print(d1)
