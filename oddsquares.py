

def oddsquares(test):
    l=[]
    sum=[]
    
    for i in range(test):
        l.append(int(input()))
        sum.append(0)
    
    for i in range(test):
        for j in range(1,l[i]+1):
            if(j%2!=0):
                sum[i] = sum[i] + ((l[i]-j+1)*(l[i]-j+1))
    
    for i in range(test):
        print(sum[i],end='\n')
            

test=int(input())
oddsquares(test)




        
        
