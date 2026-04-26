# local = neighbours - minumum = neighbours
# find any value which is smaller than its neighbours
# so in array 4,3,6 - 3 is the local minima because its lower than its immediate neighbours
# so if the oth element in array is less than the first it is minima
# so if the nth element in array is less than n-1 element then it is minima
# and for elements in between at any index i if  val[i] < v[i+1] and val[i] < v[i-1]
# is there a way to not have separate if conditions for first and last
# Brute force loop through all elements 
#But there is an efficient solution using binary search also
# Lets say for any index or any local minima - what is the possibility that we are going to 
# find a next local minima on its right side
# Example we are on index 4 with value 10
# 20,25,10,15
# here 10 is local minima because it is lower than both its neighbours
# however if we think what is the possibility that we will find another local minima in its rhs, so what could be the patterns of value we get in right
# 1) 20,25,10,15,17,19,30,40 - if the value keep increasing after 10 then there is no local minima
# 2) 20,25,10,15,14,13,5 - if values keep decresing then there is local minima
# 3) 20,25,10,15,14,13,5,30 - if values keep decreasing and increasing there there is local minima
# 4) 20,25,10,15,17,19,30,40,20,25 - if values keep increasing and decreasing and increasing then there is local minima
# so case 2,3,4 can find local minima but case 1 cannot
# Now lets think of the left side
# if value keeps increasing then it is the only local minima
# if value keeps decreasing then also we will be able to find a local minima
# if value increase decrease, or decrease increase then also we will find local minima

# So right may have an answer but left will have an answer

# Positive cases where we will get a local minima
# case 1) m is less than m-1 and m+1 , so return m
# case 2) m is less then m-1 and greater then m+1, so there is slant to right, here also we will get LM as at some point it will increase then that point is local minima or if it keeps decreasing then the last element will be local minima
# case 3) m is less them m+1 and greater then m-1, so there is slant to left side, here also we will get local minima in both cases
# case 4) m is greater then m+1 and m-1 both, so both m+1 and m-1 can be local minima, but there are more chances if we proceed towards m-1 side

def local_minima(A):
    # if empty array return -1
    if not A:
        return -1
    # if array contains 1 element return 0th index
    if len(A) == 1:
        return 0
    # if 0th element is minima return it
    if A[0] < A[1]:
        return 0
    # if last element is minima return it
    alen = len(A)
    alen -= 1
    if A[alen] < A[alen-1]:
        return alen
    # now use binary search logic to find the local minima
    lo = 1
    hi = alen-1
    # as we have eliminated the edge cases of 0th and nth index
    # there must be a solution where in index is lower than both its neighbours
    while lo <= hi:
        mid = (lo+hi)//2
        print(lo,mid, hi)
        # if the mid index is less then both mid+1 and mid-1 indexes means minima found return mid
        if A[mid] < A[mid-1] and A[mid] < A[mid+1]:
            return mid
        # if mid is in between, greater than left and lesser than right i.e. ascent on right, jump to left
        elif A[mid] > A[mid-1] and A[mid] < A[mid+1]:
            hi = mid-1
        # if mid is in between where left is hihger and right is lower i.e. descent on right, then jump to right 
        elif A[mid] < A[mid-1] and A[mid] > A[mid+1]:
            lo = mid+1
    return -1

print(local_minima([0,4,2,3,4,5,1]))
