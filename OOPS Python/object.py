class Student:
    def __init__(self):
        self.name='Rakesh'
        self.rollno=25
        self.marks=90
    def talk(self):
        print('Hello I am ',self.name)
        print('My rollno is ',self.rollno)
        print('I have Scored ',self.marks)
        
s1=Student()
s2=Student()
print(s1.talk())



