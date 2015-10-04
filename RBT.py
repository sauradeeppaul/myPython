global h1,k1
h1=[]
k1=[]

class node:
    def __init__(self,key):
        self.key=key
        self.left=0
        self.right=0
        self.par=0
        self.color=0 #color black

inordered=[]
       
class RBT:
    def __init__(self):
        self.root=0
        
    def in_order_leaves(self,a):
        if a==0:
            return
        self.in_order_leaves(a.left)
        if a.left==0 and a.right==0:
            k1.append(a)
        self.in_order_leaves(a.right)
        
    def lrotate(self,x):
        y=x.right
        y.par=x.par
        if y.par==0:
            self.root=y
        else:
            if x.par.left is x:
                x.par.left=y
            else:
                x.par.right=y
        x.par=y
        x.right=y.left
        if x.right!=0:
            x.right.par=x
        y.left=x
    
    def rrotate(self,x):
        y=x.left
        y.par=x.par
        if y.par==0:
            self.root=y
        else:
            if x.par.left is x:
                x.par.left=y
            else:
                x.par.right=y
        x.par=y
        x.left=y.right
        if x.left!=0:
            x.left.par=x
        y.right=x
    
    def insert(self,key):
        newnode=node(key)
        if self.root==0:
            self.root=newnode
            return
        else:
            x=0
            y=self.root
            while y!=0:
                x=y
                if newnode.key<y.key:
                    y=y.left
                else:
                    y=y.right
                    
            newnode.par=x
            newnode.color=1
            newnode.right=0
            newnode.left=0
            
            if newnode.key<x.key:
                x.left=newnode
            else:
                x.right=newnode
                
            self.fix_insertion(newnode)
            return
    
    def fix_insertion(self,x):
        #Case 1
        if x.par==0:
            return
        if x.par.par==0:
            return
        #x.color=1    
        #while x.par is not self.root:
        while x.par.par!=0 and x.par.color==1:
            #Case 3
            if x.par==x.par.par.left:
                if x.par.par.right.color==1 and x.par.color==1: #x's uncle
                    x.par.color=0
                    x.par.par.right.color=0
                    x.par.par.color=1
                    x=x.par.par
                
                else:
                    if x.par.right==x:
                        x=x.parent
                        self.lrotate(x)
                    x.par.color = 0
                    x.par.par.color = 1
                    self.rrotate(x.par.par)
                    
            if x.par==x.par.par.right:
                if x.par.par.left.color==1:
                    x.par.color=0
                    x.par.par.left.color=0
                    x.par.par.color=1
                    x=x.par
                    
                else:
                    if x.par.left==x:
                        x=x.parent
                        self.rrotate(x)
                    x.par.color = 0
                    x.par.par.color = 1
                    self.lrotate(x.par.par)
        self.root.color=0
        return
    
    def height_array(self):
        self.in_order_leaves(self.root)
        for i in range(len(k1)):
            count=0
            while k1[i]!=self.root:
                count+=1
                print (k1[i]).key
                k1[i]=k1[i].par
            h1.append(count)

    def height(self,value=None):
        if value==None:
            if len(h1)==0:
                self.height_array()
            print h1
            maxh=h1[0]
            for j in range(len(h1)):
                if h1[j]>maxh:
                    maxh=h1[j]
            print 'maximum height of avl='
            return maxh

        else:
            r=self.root
            if r.key==value:
                count=0
            else:    
                count=0
                while (r.key!=value and r!=0):
                    p=r                
                    if value<r.key:
                        r=r.left
                    else:
                        r=r.right
                    count=count+1
            print 'height of node in avl='
            return count

    def avg_height(self):
        if len(h1)==0:
            self.height_array()
        total=0
        #print(len(h))
        for k in range (len(h1)):
            total=total+h1[k]
        avg=total/(len(h1))
        print 'average height of avl = '
        return avg
    
t=RBT()
t.insert(3)
t.insert(1)
t.insert(9)
t.insert(4)
t.insert(6)
t.insert(0)
t.insert(7)
t.insert(2)
print t.root.key,'*'
print t.root.left.key
print t.root.right.key
#print t.root.right.left.key
#print t.root.right.right.key
print t.height()
print t.avg_height()
