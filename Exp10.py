'''
Implementation of Multithreaded program
'''
from threading import *
from time import sleep

class A(Thread):
    def run(self):
        for i in range(50):
            print('A')

class B(Thread):
    def run(self):
        for i in range(50):
            print('B')


def main():
    a = A()
    b = B()
    a.start()
    #sleep(0.1)
    b.start()
    a.join()
    b.join()
    print('Done')

if __name__=='__main__':
    main()