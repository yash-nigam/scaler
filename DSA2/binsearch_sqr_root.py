# Q2. Square Root of Integer
# Given an integer A. Compute and return the square root of A.
# If A is not a perfect square, return floor(sqrt(A)).

# NOTE: 
#    The value of A*A can cross the range of Integer.
#    Do not use the sqrt function from the standard library. 
#    Users are expected to solve this in O(log(A)) time.
# Problem Constraints 0 <= A <= 109
# Input Format\
# The first and only argument given is the integer A.
# Output Format
# Return floor(sqrt(A))
# Example Input
# Input 1:
#  11
# Input 2:
#  9
# Example Output
# Output 1:
#  3
# Output 2:
#  3

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        # square root of A
        # start with left most index as 1 and rightmost as A
        # calculate mid, calculate mid square, i
        # if midsqaure <= A save ans = mid sqaure, lo = mid+1
        # if midsquare > A then hi = mid-1
        # return mid

        # edge cases if is 0 there cant be any sq root of 0
        if A == 0: 
            return 0
        # edge case if A is 1 only 1 is the square root of 1
        if A == 1: 
            return 1
        
        hi=A
        lo=1
        ans = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if mid*mid <= A:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return  ans