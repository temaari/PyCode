class Student:
    degree = "CS"
    def __init__(self, name="", age=0, job=None):
        self.name = name
        self.age = age
        self.job = job
        self.school = "AUT"

    def getInfo(self):
        print (self.name,"Did a fantastic job at Coding today.",self.name,"is such a wonderful student")
        
    def setName(self, name):
        self.name = name

class Main:
    def __init__(self):
        k = Student("John",5,None)
        k.getInfo()
        
m = Main()
input()
