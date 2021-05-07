#Experiment 3, Program 3.2
#Program to implement Constructors

class Student:
    no_of_courses=5
    credits=25
    
    def __init__(*arg):
        if(len(arg)>1):
            if isinstance(arg[1],Student):
                arg[0].rollno=arg[1].rollno   #instance var
                arg[0].name=arg[1].name
                arg[0].addr=arg[1].addr
                arg[0].mob=arg[1].mob
            else:
                arg[0].rollno=arg[1]   #instance var
                arg[0].name=arg[2]
                arg[0].addr=arg[3]
                arg[0].mob=arg[4]
        else:
            arg[0].rollno=arg[0].name=arg[0].addr=arg[0].mob=None
        '''
    def __init__(self,r=None,n=None,a=None,m=None):
        self.rollno=r
        self.name=n
        self.addr=a
        self.mob=m
        '''
    def setval(self,rollno,name,addr,mob):
        self.rollno=rollno
        self.name=name
        self.addr=addr
        self.mob=mob
    def getval(self):
        #print('Self is at',id(self))
        return self.rollno, self.name, self.no_of_courses, self.credits, self.mob, id(self)
    @classmethod
    def setcourses(cls,n):
        cls.no_of_courses=n
    @classmethod
    def setcredits(cls,c):
        cls.credits=c
    @staticmethod
    def is_workday(day):
        if day.weekday()==6:
            return False
        return True

#driver code
def main():
    s=Student('19CO50','Khan Aftab','New Panvel',9898989898)
    #s.setval('19CO10','Ansari Wasim','Panvel',9898929292)
    print(s.getval())
    s.setcourses(7)
    print(s.getval())
    s1=Student()
    #s1.setval('19CO20','Khan Wasim','Mumbai',9898929292)
    print(s1.getval())
    s1.setcredits(30)
    print(s.getval())
    print(s1.getval())
    import datetime
    d=datetime.date(2021,3,3)
    print('Is workday ?',Student.is_workday(d))
    s2=Student(s1)
    print(s2.getval())
    s3=s1
    print(s3.getval())


if __name__=='__main__':
    main()