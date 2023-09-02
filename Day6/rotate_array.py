# rotate array
def rotate1(Arr):
    tmp=Arr[len(Arr)-1]
    print(f"Last elem={tmp}")
    count= len(Arr)-1
    while(count>0):
        Arr[count]=Arr[count-1]
        count-=1
    Arr[0]=tmp    
    return Arr
A=[6,3,9,4]
print("--------")
print(A)
print("--------")
print(rotate1(A))
print(rotate1(A))
print(rotate1(A))
print(rotate1(A))
# array will rotate and come back to same values in len(Arr) rotations/
