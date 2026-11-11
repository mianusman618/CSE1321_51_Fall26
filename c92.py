class Student:
    def __init__(self,id,GPA,Major,Name):
        self.id=id
        self.GPA=GPA
        self.Major=Major
        self.Name=Name
    def register_course(self,c_name="abc"):
        if c_name=="abc":
            print("This is default course")
        else:
            print("Registering ", c_name)
    def print_info(self):
        print(f"Name = {self.Name} \n id = {self.id}\n GPA = {self.GPA} \n Major = {self.Major}")


s1=Student(1,3.0,"CS","Alice")
s1.print_info()
s2=Student(2,3.5,"SE","Bob")
s2.print_info()
