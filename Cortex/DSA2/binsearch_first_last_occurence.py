#Given a sorted array of integers A (0-indexed) of size N, find the left most and the right most index of a given integer B in the array A.

#Return an array of size 2, such that 
#          First element = Left most index of B in A
#          Second element = Right most index of B in A.
#If B is not found in A, return [-1, -1].
#Note : Note: The time complexity of your algorithm must be O(log n)..
# Output Format
# Return the left most and right most index (0-based) of B in A as a 2-element array. If B is not found in A, return [-1, -1].
# Example Input
# Input 1:
#  A = [5, 7, 7, 8, 8, 10]
#  B = 8
# Input 2:
#  A = [5, 17, 100, 111]
#  B = 3
# Example Output
# Output 1:
#  [3, 4]
# Output 2:
#  [-1, -1]
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        # finding the leftmost and rightmost index of a given integer in an sorted array
        # so if there is only one such integer then both left and right would be the same
        # if there is no occurence then -1,-1
        # so the simplest logic here would be first find that integer using binary search
        # as soon as the first integer is found, simply to a linear search to the left and then to the right 
        # 10,10,10,10,10]
        #  1,2 ,3 ,4 ,5 
        if len(A) == 1:
            return [0,0]
        lo=0
        hi=len(A)-1
        found = -1
        while lo <= hi:
            mid=(lo+hi)//2
            if A[mid] == B:
                found=mid
                break
            elif A[mid] > B:
                hi = mid-1
            else:
                lo = mid+1
        if found == -1:
            return [-1,-1]
        #return [mid,mid]
        first,last=mid,mid
        # increment to the left by 1 if left side = B 
        while A[first-1] == B and first-1>=0:
            first -= 1
        # increment to right by 1 if right =B
        while last+1 < len(A): 
                if A[last+1] == B:
                    last += 1
                else:
                    break
        return[first,last]
        


        

