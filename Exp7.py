'''
Exp 7: GUI Program using tkinter
'''
from tkinter import *

class App:
    def __init__(self):
        self.root=Tk()
        self.root.title('GUI App')
        self.root.geometry('500x350')
        self.root.configure(background='light blue')
        #Labels are created
        self.rollno = Label(self.root, text="Roll No.", bg="light blue")
        self.name = Label(self.root, text="Name", bg="light blue")
        self.address = Label(self.root, text="Address", bg="light blue")
        self.mob = Label(self.root, text="Mobile", bg="light blue")
        #Labels are added on window
        self.rollno.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.address.grid(row=2,column=0)
        self.mob.grid(row=3,column=0)
        #Textfields are created
        self.rollnof = Entry(self.root)
        self.namef = Entry(self.root)
        self.addressf = Entry(self.root)
        self.mobf = Entry(self.root)
        #Textfields are added on window
        self.rollnof.grid(row=0,column=1,ipadx='100')
        self.namef.grid(row=1,column=1,ipadx='100')
        self.addressf.grid(row=2,column=1,ipadx='100')
        self.mobf.grid(row=3,column=1,ipadx='100')
        #Submit button created and added on window
        self.submit = Button(self.root, text="Submit", fg="Black", bg="light green", command=self.insert) 
        self.submit.grid(row=8, column=1,sticky=W+E)
        #Clear button created and added on window
        self.clear = Button(self.root, text="Clear",fg="Black", bg="light green", command=self.clearAll) 
        self.clear.grid(row=8, column=0,sticky=W+E)  
        self.root.mainloop()
    def insert(self):
        with open('student.csv','a') as file:
            rec=self.rollnof.get()+','+self.namef.get()+','+self.addressf.get()+','+self.mobf.get()+'\n'
            #rec=self.rollnof.get()+';'
            file.write(rec)

        
    def clearAll(self):
        self.rollnof.delete(0,'end')
        self.namef.delete(0,'end')
        self.addressf.delete(0,'end')
        self.mobf.delete(0,'end')

def main():
    myapp = App()

if __name__=='__main__':
    main()
