# Binary search
# Expected a sorted array
# start with start =0 and end = n
# calculate mid
# if mid is less then target, mid+1 = low
# if mid is higher than target, mid-1 is high
# 
def binary_search(A,target):
    start,end=0,len(A)-1
    loop_count = 0
    while start <= end:
        loop_count += 1
        #print(loop_count)
        mid = (start+end)//2
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            start = mid + 1
        elif A[mid] > target:
            end = mid - 1
    return -1

# now how to use the same approach to find the first occurence of a number in a sorted string
# first occurence means that there can be more than one occurences of that number
# Brute Force will also work but that will require n iterations

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,12,12,12,12,12,12,12,13,14,15,16,17,18,19,20],12))
# lo =0 hi = n = 27 mid = 13 A[13] = 12 so match found
# but we dont know if this is the first occurence, it could be and it could be noe
# so we save it in a var as ans=13 
# There could be an smaller index with same answer, so we want to explore on left hand side
# if we wanted to find the largest index then we would have gone to right
# 12 is found at mid index 13, so now put hi as mid-1 = 12
# so start = 0 , end = 12, mid = 6, A[6] = 7, 7 < 12 so 
# start = 8 end = 12, mid =10 A[10] = 11, 11< 12 so
# start = 11, end = 13, 12, mid = 12 so mid is A[12] = 12 so again our target is found so save it in ans
def binary_search_first(A,target):
    start,end=0,len(A)-1
    loop_count = 0
    ans = -1
    while start <= end:
        loop_count += 1
        #print(loop_count)
        mid = (start+end)//2
        if A[mid] == target:
            ans = mid
            end = mid-1
        elif A[mid] < target:
            start = mid + 1
        elif A[mid] > target:
            end = mid - 1
    return ans
print(binary_search_first([1,2,3,4,5,6,7,8,9,10,11,12,12,12,12,12,12,12,12,13,14,15,16,17,18,19,20],12))