class Person:
    def __init__(self,name,number):
        self.name=name
        self.number=number

    def PrintInfo(self):
        print(self.name, self.number)
    def PrintPersonData(self):
        print("Person : {0},{1}".format(self.name,self.number))

class Student(Person):
    def __init__(self,name,number,subject,studentid):
        Person.__init__(self,name,number)
        self.subject=subject
        self.studentid=studentid

    def PrintID(self):
        print(self.name, self.number)
        print(self.subject, self.studentid)


class Super:
    x=10
    def PrintX(self):
        print(self.x)
class Sub(Super):
    y=20
    def PrintY(self):
        self.b=1000
        print(self.y)





