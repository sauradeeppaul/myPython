# input plain msg m is always less than n
# e and phi should be coprime
# p and q are prime and shud nt be equal

global encrypt,decrypt
encrypt=[]
decrypt=[]

def simple_gcd(a,b):
    if b==0:
        return a
    else:
        return simple_gcd(b,a%b)

def full_gcd(a,b):
    if b==0:
        return [a,1,0]
    else:
        d1,x1,y1=full_gcd(b,a%b)
        d,x,y=(d1,y1,x1-((a/b)*y1))
        return [d,x,y]

def find_d(a,b):
    d,x,y=full_gcd(a,b)
    if y>0:
        return y
    else:
        y+=a
        return y

def find_e(phi):
    e=3
    while e<phi:
        if simple_gcd(e,phi)!=1:
            e+=1
        else:
            return e

def rsa(p,q,ip):
    n=p*q
    phi=(p-1)*(q-1)
    e=find_e(phi)
    d=find_d(phi,e)
    encry=(ip**e)%n
    encrypt.append(encry)
    decry=(encry**d)%n
    decrypt.append(decry)

def inputf(filename,p,q):
        a=open(filename,'r') #open a file
        lines=a.readlines()
        alist=[]
        for i in range(len(lines)):
            lines[i]=int(lines[i])
        for line in lines:
            alist.append(line)
        for a in alist:
            rsa(p,q,a)

def output(filename):
    let=inputf(filename,61,53) # FIXING P AND Q HERE.
    a=open('encrypted.txt','w') # open a file in write mode
    b=open('decrypted.txt','w') # open a file in write mode
    for i in encrypt:
        a.write('%s\n' %i )
    a.close()
    for j in decrypt:
        b.write('%s\n' %j)
    b.close()

print output('new_1.txt')
