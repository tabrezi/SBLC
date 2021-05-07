'''
1.2	Write a python program to implement List, Set, Tuple, Dictionary and Array.
Theory
@author: Name (RollNo)
'''
from array import *

#List
'''
List Theory
'''
print( "---------------LIST -----------------")
print( "")
l=[12,23,-5,0.8,'python',"CO"] #Creating a list of variable datatypes
print("printing original list",l) #printing list
print("printing first three elements of a list", l[0:3]) #printing first three elements of a list
print("printing Last elements of a list",l[-1]) #printing Last elements of a list
print("printing first three elements of a list twice",l[0:3] * 2) #printing first three elements of a list twice
print( "")
print ("---------------LIST FUNCTIONS-----------------")
print( "")
l1=list(range(1,8)) #Creating a list of range 1 to 7
print ("List of range 1 to 7", l1)
l1.append(9) #append 9
print ("Append 9 :",l1)
l1.sort(reverse=True)
print("Descending Sort:",l1)
l1.sort()
print ("Ascending Sort:",l1)
l1.reverse()
print("Reverse:",l1)
l1.sort()
l1.remove(9)
print("Remove 9:",l1)
print("count:",l1.count(5))
print("max:",max(l1))
print("min:",min(l1))
print("Index of 6:",l1.index(6))

#Tuple
'''
Tuple Theory
'''
print("--------TUPLE DATATYPE (READ ONLY LIST)------------")
print("")
tpl=(-5,0.8,'python',"CO") #Creating a Tuple
print("Created Tuple is ", tpl)
print("Tuple elements 0 to 2 is", tpl[0:2]) #printing first two elements of a touple
print("")
print("--------TUPLE FUNCTIONS -----------")
tpl2=(10,20,30,40,10,20,10) #Creating a Tuple2
print("Created Tuple2 is ",tpl2)
print("Length : ", len(tpl2))
print("Min : ", min(tpl2))
print("Max : ", max(tpl2))
print("Count no. of 10's: ", tpl2.count(10))
print("Reverse Sort : ", sorted(tpl2,reverse=True))
print("")
#Set
'''
Set Theory
'''
print( "---------------SET -----------------")
print( "")
s1={1,2,3,4,5,80,4,10,12,2}
s2=set()
s3={1,1.2,'aiktc'}
print(s1,s2,s3)
s1.add(60)
print(s1,s1.issuperset(s2))
print(s1.union(s3))

#Dict
'''
Dictionary Theory
'''
print("--------DICTIONARIES i.e. key:value pair------------")
print("")
d1={'Name':"Ahmed",'gender':"M",'age':20,'college':"AIKTC"} #create dictionary
print("print dictionary: ",d1)
print("")
print("-->Keys :",d1.keys())
print("-->Values :",d1.values())
print("-->Keys and values :",d1.items())
d1.update({'Name':"Sachin"})
print("-->Print updated dictionary: ",d1)

#Array
'''
Array Theory
'''
print("---------------ARRAYS -----------------")
print("")
arr=array('i',[10,20,30,40,50]) #Create array with integer values
print("The Array Elements are")
for i in arr: #i is element and arr in array name
    print(i) #Requires indentation
print("length of array is",len(arr))
arr1=array('u',['a','b','c','d']) #Create array with character values
print("The Character Array Elements are")
for i in arr1: #i is element and arr in array name
    print(i) #Requires indentation
'''
Conclusion: 
'''