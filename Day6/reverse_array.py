# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
def swap(Arr, A, B):
    tmp=Arr[A]
    Arr[A]=Arr[B]
    Arr[B]=tmp
    return Arr
    
Arr=[1,2,3,4,5,6,7,8]
l=0
r=len(Arr)-1
while(l<r):
    print(f"Swap index l={l} val={Arr[l]} with index r={r} val{Arr[r]}")
    print(swap(Arr,l,r))
    l+=1
    r-=1

