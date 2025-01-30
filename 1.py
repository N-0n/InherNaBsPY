#parent class
class person():
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def disp(self):
        print(self.name)
        print(self.age)
        
#child class
class employee(person):#employee is child class of person
    def __init__(self, n, a,s,d):
        self.sal=s
        self.designation=d
        person.__init__(self,n,a)
        super().__init__(n,a)
        print(self.sal)
        print(self.designation)

o1=employee("Devanshu",31,64000,'Officer')
o1.disp()
