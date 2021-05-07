'''
Program 4.1: Implementation of Inheritance
'''

class Person:
    def __init__(self,n=None,a=None,m=None):
        self.name=n
        self.addr=a
        self.mob=m
    def getval(self):
        return self.name,self.addr,self.mob

class Student(Person):
    def __init__(self,r=None,n=None,a=None,m=None,sgpi=None):
        self.rollno=r
        self.sgpi=sgpi
        Person.__init__(self,n,a,m)     #initialize the instance vars inherited from base class
    def getstud(self):
        return self.rollno,self.name,self.sgpi


#driver code
def main():
    p=Person('Ahmed','Mumbai',9898989898)
    print(p.getval())
    s=Student('19CO45','Sachin','Panvel',989898,8.8)
    print(s.getstud())

if __name__=='__main__':
    main()