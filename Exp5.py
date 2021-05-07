'''
Implementation of Stack, Queue and Linked List
'''
from collections import deque

#Stack using list

class Stack:
    def __init__(self,d=None):
        if d==None:
            self.data=list()
        else:
            self.data=d
    def isEmpty(self):
        if len(self.data)==0:
            return True
        return False
    def push(self,d):
        self.data.append(d)
    def pops(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            return self.data.pop(0)
            
    def display(self):
        if self.isEmpty():
            print('Stack is Empty.')
        else:
            print('Stack Content:')
            for i in range(len(self.data)-1,-1,-1):
                print(self.data[i])

#Node for linked list
class Node:
    def __init__(self,d=None,n=None):
        self.data=d
        self.next=n
    
#Linked list class
class LinkedList:
    def __init__(self,h=None):
        self.head=h
    def insert(self,d):
        newnode=Node(d)
        if self.head==None:
            self.head=newnode
            #print('M here:',newnode,self.head)
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=newnode
    def display(self):
        #print(self.head)
        if self.head==None:
            print('Linked List is Empty.')
        else:
            temp=self.head
            print('Linked List Contents:')
            while temp:
                print(temp.data)
                temp=temp.next
            


def main():
    st=Stack([10,20,30]);
    st.display()
    st1=Stack()
    st1.display()
    st1.push(50)
    st1.push(60)
    st1.display()
    print('Popping:',st1.pops())
    st1.display()
    print('Popping:',st1.pops())
    st1.display()

    #Queue using deque
    q=deque([10,20,30])
    print('Queue is:',q)
    q.append(40)
    print('Queue is:',q)
    print('Deleting:',q.popleft())
    print('Queue is:',q)

    #Linked List
    l=LinkedList()
    l.insert(10)
    l.display()
    l.insert(20)
    l.insert(30)
    l.display()


  


if __name__=='__main__':
    main()