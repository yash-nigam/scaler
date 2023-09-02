def rev(arr, l, r):
    c= len(arr)-1
    while(l<r):
        tmp=arr[r]
        arr[r]=arr[l]
        arr[l]=tmp
        l+=1
        r-=1
    return arr
a=[4,6,5,7,1,4,2,5]
k=2
print(rev(a,0,len(a)-1))
print(rev(a,0,k-1))
print(rev(a,k,len(a)-1))
