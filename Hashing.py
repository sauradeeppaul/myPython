import string
import random
import math
import time


def reset(n,hashtable):
    hashtable=[]
    for x in range(0,n): #Creating a base 36 integer list corresponding to the string list
        hashtable.append([])
    return hashtable

def division_method(nums,lines,hashtable):
    '''Uses division method to hash'''
    #t=time.time()
    n=len(lines)
    for i in range(0,len(lines)):
        x=nums[i]
        hashtable[x%n].append(lines[i])
    return #time.time()-t
    
def multiplication_method(nums,lines,hashtable):
    '''Uses multiplication method to hash'''
    t=time.time()
    a=random.random()
    n=len(lines)
    for i in range(0,n):
        x=nums[i]
        x*=a
        x%=1
        x*=n
        x=int(math.floor(x))
        hashtable[x].append(lines[i])
    return time.time()-t
    
def linear_probing(nums,lines,hashtable):
    '''probes linearly with a universal hash function'''
    t=time.time()
    n=len(lines)
    a=random.randint(1,n)
    b=random.randint(1,n)
    for i in range(0,len(lines)):
        x=nums[i]
        X=(a*x+b)%n
        fill=0
        while fill==0:
            if len(hashtable[X])==0:
                fill=1
                hashtable[X]=lines[i]
            else:
                X=((X+1)%(n+1))%n
    return time.time()-t
    
def quadratic_probing(nums,lines,hashtable):
    '''probes quadratically with a hash function'''
    t=time.time()
    n=len(lines)
    a=random.randint(1,n)
    b=random.randint(1,n)
    for i in range(0,len(lines)):
        x=nums[i]
        X=(a*x+b)%n
        fill=0
        t=0
        while fill==0:
            if len(hashtable[X])==0:
                fill=1
                hashtable[X]=lines[i]
            else:
                X=((X+t**2)%(n+1))%n
                t+=1
    return time.time()-t
    
def double_hashing(nums,lines,hashtable):
    '''Uses two universal hash functions and hsahes the file'''
    t=time.time()
    n=len(lines)
    a1=random.randint(1,n)
    b1=random.randint(1,n)
    for i in range(0,len(lines)):
        x=nums[i]
        X1=(a1*x+b1)%n
        fill=0
        t=0
        while fill==0:
            if len(hashtable[X1])==0:
                fill=1
                hashtable[X1]=lines[i]
            else:
                a2=random.randint(1,n)
                b2=random.randint(1,n)
                X2=(a2*x+b2)%n
                X1=((X1+t*X2)%(n+1))%n
                t+=1
    return time.time()-t

def starthash():
    '''Function to start hashing of a text file'''
    text_file = open("test2.txt", "r") #Extracting text to an array
    lines = text_file.read().split(' ')

    newlines=[]
    for i in range(0,len(lines)): #Converting all letters to their respective lowercase forms
        lines[i]=lines[i].lower()
        newlines.append('')
        for a in lines[i]:
            if a.isalpha():
                newlines[i]+=a
        
    countempty=0
    
    for a in newlines: #Counting number of empty elements
        if a=='':
            countempty+=1
               
    for i in range(0,countempty): #Removing all empty elements
        newlines.remove('')
    
    hashtable=[]
    numbers=[]
    n=len(newlines)
    for x in newlines: #Creating a base 36 ineger list corresponding to the string list
        numbers.append(string.atoi(x,36))
        hashtable.append([]) #Simultaneously creating a hashtable of the same size
    
    t1=division_method(numbers,newlines,hashtable)
    hashtable=reset(n,hashtable)
    t2=multiplication_method(numbers,newlines,hashtable)
    hashtable=reset(n,hashtable)
    t3=linear_probing(numbers,newlines,hashtable)
    hashtable=reset(n,hashtable)
    t4=quadratic_probing(numbers,newlines,hashtable)
    hashtable=reset(n,hashtable)
    t5=double_hashing(numbers,newlines,hashtable)
    
    t=min(t1,t2,t3,t4,t5)
        
    print newlines
    print hashtable
    
    if t1==t:
        print 'Division method works the fastest'
    elif  t2==t:
        print 'Multiplication method works the fastest'
    elif  t3==t:
        print 'Linear probing works the fastest'
    elif  t4==t:
        print 'Quadratic probing works the fastest'
    elif  t5==t:
        print 'Double hashing works the fastest'  

starthash()