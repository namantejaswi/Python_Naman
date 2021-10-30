

def binarysearch(arr,target):
    
    low=0
    high=len(arr)-1
    
    while(low<=high):
        
        mid=int((low+high)/2)
        
        if(arr[mid]==target):
            return mid
        
        elif(arr[mid]<target):
            
            low=mid+1            
                
        elif(arr[mid]>target):
            high=mid-1
    
            
l=[2,3,4,5,8,9,11,44,103,124,202,333] 
print(binarysearch(l,11))

print(binarysearch(l,124))

print(binarysearch(l,44))

