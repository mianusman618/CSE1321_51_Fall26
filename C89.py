class Student:
    id=0
    GPA=0
    Major=""
    Name=""

    def register_course(self,c_name="abc"):
        if c_name=="abc":
            print("This is default course")
        else:
            print("Registering ", c_name)
    def print_info(self):
        print(f"Name = {self.Name} \n id = {self.id}\n GPA = {self.GPA} \n Major = {self.Major}")


s1=Student()
s2=Student()
s1.print_info()
s1.Name="Alice"
s1.id=123
s1.GPA=3.0
s1.Major="CS"
s1.print_info()
print("Printing S2")
s2.print_info()
s1.register_course("CSE1321")
s2.register_course()