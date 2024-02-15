class Students:
    def __init__(self,name,rollno,clss):
        self.name=name
        self.rollno=rollno
        self.clss=clss
    def info(self):
        print('Student name :',self.name)
        print('Roll No :',self.rollno)
        print('Class :',self.clss)
        
list_of_student=[]

while True:
    name=input('Enter Student name :')
    rolllno=input('Enter RollNo :')
    clss=input('Enter class :')
    stud=Students(name,rolllno,clss)
    list_of_student.append(stud)
    print('Student added Successfully')
    option=input('do you want to add one more Student [Yes|No]')
    
    if option.lower()=='no':
        break
    
print('All Student in this School') 
print('#'*20)

for S in list_of_student:
    S.info() 