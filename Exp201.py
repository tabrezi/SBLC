'''
2.1	Write a python program to implement loops in Python.
Theory
@author: Name (RollNo)
'''

#factorial using for loop
num=int(input('Enter the Number:'))
fact=1
for i in range(1,num+1):
    fact=fact*i
print('Factorial of',num,'is',fact)

#fibonacci using while loop
num=int(input('Enter the Number:'))
a=0
b=1
c=a+b
print('Fibonacci Series till',num,':',a,'\t',b,end='')
while(c<=num):
    print("\t",c,end='')
    a=b
    b=c
    c=a+b


'''
Conclusion: 
'''