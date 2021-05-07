'''
File handling in Python
'''

#file=open('Sess9.py','r')
'''
#cont=file.read()
#print(cont)
print('_______________________')
line=file.readline()
line=file.readline()
print(line)
'''
with open('Sess9.py','r') as file:
    lines=file.readlines()
    cnt=wcnt=0
    for l in lines:
        word=l.split()
        print(word,len(word))
        wcnt+=len(word)
        cnt+=1
    print('Number of Lines:',cnt,'and Number of Words:',wcnt)
#file.close()

#file=open('Sam','a')
with open('Sam','a') as file:
    #file.write('This is a content of a sample file.\n')
    file.write('\nThis is a only line again and again.')
    
#file.close()