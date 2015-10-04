tower=[[],[],[],[]]  #Creating a list with four empty pegs
iter=0

def shiftdisk(initial, final):
    '''Shifts the top disk from the initial disk to the final disk'''
    global iter
    iter+=1
    temp=tower[initial][len(tower[initial])-1]
    tower[initial].pop(len(tower[initial])-1)
    tower[final].append(temp)
    print 'Tower after ',iter,' iteration(s)'
    print tower

def solve(disk, initial, temp1, temp2, final):
    '''Disk that solves the problem for a given number of disk'''
    if disk == 1:
        shiftdisk(initial, final)
    elif disk == 2:
        shiftdisk(initial, temp1)
        shiftdisk(initial, final)
        shiftdisk(temp1, final)
    else:
        solve(disk - 2, initial, temp2, final, temp1)
        shiftdisk(initial, temp2)
        shiftdisk(initial, final)
        shiftdisk(temp2, final)
        solve(disk - 2,  temp1, initial, temp2, final)

def initialize():
    '''Resets the setup'''
    n=input('Enter number of disks: ')
    for i in range(0,n):
        tower[0].append(i+1)
    tower[0].reverse()

def solvetower():
    initialize()
    print tower
    solve(len(tower[0]),0,1,2,3)
    
solvetower()   