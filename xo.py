from platform import win32_edition


def check(arr):
    win=0
    sum=0
    for i in range(len(arr)):
            sum=0
            count=arr[i][0]
            for j in range(len(arr[i])):
                    if(count == arr[i][j] and count!='__'):
                        sum+=1
            if(sum==3):
                win=1
                break
    
    for i in range(len(arr)):
            sum=0
            count=arr[0][i]
            for j in range(len(arr[i])):
                    if(count==arr[j][i] and count!='__'):
                        sum+=1
            if(sum==3):
                win=1
                break
    
    for i in range(len(arr)):
            sum=0
            count=arr[0][0]
            for j in range(len(arr[i])):
                    if(count==arr[i][j] and i==j and count!='__'):
                        sum+=1
            if(sum==3):
                win=1
                break
    for i in range(2,0,-1):
            sum=0
            count=arr[0][i]
            for j in range(2,0,-1):
                    if(count==arr[i][j] and i+j==2 and count!='__'):
                        sum+=1
            if(sum==3):
                win=1
                break
    
    
    if(win==1):
        print("won")
        exit(0)
    

def printarr(arr):
    for i in range(len(arr)):
            for j in range(len(arr[i])):
                print(arr[i][j],end=' ')
            print(end='\n')                         

def xo(x,temp):
    arr=[['__','__','__'],['__','__','__'],['__','__','__']]
    printarr(arr)
    while x!=9:
        
        if(temp==1):
            print("enter the place of X")
            temp=0
        else:
            print("enter the place of O")
            temp=1
        
        p=int(input())
        q=int(input())
        
            
        for i in range(3):
            for j in range(3):
                if(i==p and j==q):
                    if(temp==0):
                        arr[i][j]='X'
                        x+=1
                    else:
                        arr[i][j]='O'
                        x+=1
        printarr(arr)  
        check(arr)
    if(x==9):
        print("draw")
        exit(0)
    


x,temp=0,0      
xo(x,temp)

         
