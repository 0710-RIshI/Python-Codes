def mergesort(arr):
    if len(arr)>1:
            
        mid =len(arr)//2
        l=arr[:mid]
        r=arr[mid:]
        i=j=k=0
        mergesort(l)
        mergesort(r)
        while(i<len(l) and j<len(r)):
            if(l[i]<r[j]):  
                arr[k]=l[i]
                i+=1
            else:
                arr[k]=r[j]
                j+=1
            k+=1
        
        while(i<len(l)):
            arr[k]=l[i]
            i+=1
            k+=1
        while(j<len(r)):
            arr[k]=r[j]
            j+=1
            k+=1
        
        


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i],end='\n')


if __name__=='__main__':
    arr=[5,6,4,3,7,8,1]
    mergesort(arr)
    printlist(arr)
        


