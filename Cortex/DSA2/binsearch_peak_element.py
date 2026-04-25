# Q4. Find a peak element
# Problem Description
# Given an array of integers A, find and return the peak element in it.
# An array element is considered a peak if it is not smaller than its neighbors. For corner elements, we need to consider only one neighbor.

# NOTE:

# It is guaranteed that the array contains only a single peak element.
# Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.


# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= A[i] <= 109
# Input Format
# The only argument given is the integer array A.
# Output Format: 
# Return the peak element.



# Example Input Input 1:

# A = [1, 2, 3, 4, 5] Input 2:
# A = [5, 17, 100, 11]

# Example Output
# Output 1:
# 5
# Output 2:
# 100
# Example Explanation
# Explanation 1:
#  5 is the peak.
# Explanation 2:
#  100 is the peak.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
    # if i = 0 and then A[i] is peak if A[i] > A[i+1]
    # if i = n then A[i] is peak if A[n] > A[i-1]
    # from 1 to n-2
    # All increasing till end 1,2,3,4,5,6 this will be covered by first case
    # All decreasing till end 5,4,3,2,1 this will be covered by seconds case
    # peak in middle
    # 5,17,100,11
    # if there is only one peak then we can increment one by one also and go ahead to find peak
    # lo=0 hi = 3 mid = 1 A[1] = 17 if i+1 = > i then lo = mid+1 , lo = 2, hi = 3 mid = 2 = 100 i+1 > i 11 > 100 no , return 100
        if len(A) == 1:
            return A[0]
        if A[0] > A[1]:
            return A[0]
        if A[len(A)-1] > A[len(A)-2]:    
            return A[len(A)-1]
        lo = 1
        hi = len(A)-2
        while lo <= hi:
            mid = (lo+hi)//2
            if A[mid] > A[mid+1] and A[mid] > A[mid-1]:
                return A[mid]
            if A[mid] <= A[mid+1]:
                lo = mid + 1
            else:
                hi = mid-1
        return A[mid]


