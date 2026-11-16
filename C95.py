class Student:
    id=0
    name=""
class classroom:
    def __init__(self):
        self.list_of_stds=[]
    def show_students(self):
        for s in self.list_of_stds:
            print(s.name)

s1=Student()
s1.name="Alice"
s2=Student()
s2.name="Bob"
s3=Student()
s3.name="Charlie"

c1=classroom()
c2=classroom()


c1.list_of_stds.append(s1)
c2.list_of_stds.append(s2)
c2.list_of_stds.append(s3)
print("C1 students")
c1.show_students()
print("C2 students")
c2.show_students()