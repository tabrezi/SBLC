'''
Exp 2.2: Implementation of functions in Python
'''
def fact(num):
    '''
    Returns the factorial of given number. This is from Session6.py
    '''
    f=1
    for i in range(1,num+1):
        f=f*i
    return f

def fibo(num):
    a=0
    b=1
    c=a+b
    print('Fibonacci Series upto',num,'is',a,'\t',b,'\t',end='')
    while c<=num:
        print(c,'\t',end='')
        a=b
        b=c
        c=a+b
    print()
    
def fibo1(num):
    a=0
    b=1
    c=a+b
    res=[0,1]
    #print('Fibonacci Series upto',num,'is',a,'\t',b,'\t',end='')
    while c<=num:
        #print(c,'\t',end='')
        res.append(c)
        a=b
        b=c
        c=a+b
    return res

def main():
    while(True):
        n=int(input('Enter the Number:'))
        print('Factorial of',n,'is',fact(n))
        #fibo(n)
        print('Fibonacci Series upto',n,':',fibo1(n))
        ch=input('\tDo u want to continue (Y/N)?')
        if (ch=='N' or ch=='n'):
            break

if __name__=='__main__':
    main()