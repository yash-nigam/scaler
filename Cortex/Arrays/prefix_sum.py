# first method is a brute force solution which calculates the sum of all sub arrays
# sum of 0 with 1, then sum of 0 with 1 & 2 and so on till n, then start at 1, sum of 1 with 2 & 3 and so on
# here 3 for loops are involved 
def range_sum(A,l,r):
    sum = 0
    for i in range(l,r+1):
            sum += A[i]
    return sum

def all_sums(A):
    for l in range(len(A)):
        r = l
        while r < len(A):
            print(range_sum(A,l,r))
            print("---")
            r += 1
          
def prefix_sum(A,l,r):
    prefix_sum = [0] * len(A)
    prefix_sum[0] = A[0]
    for i in range(1,len(A)):
        prefix_sum[i] = prefix_sum[i-1] + A[i]
        print(prefix_sum)
    print(prefix_sum[r]-prefix_sum[l-1])    
    
        

#all_sums([1,2,3,4,5,6,7,8,9,10])
prefix_sum([1,2,3,4,5,6,7,8,9,10],2,4)
print(range_sum([1,2,3,4,5,6,7,8,9,10],2,4))
