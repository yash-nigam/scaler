#Problem Description
#Find the maximum sum of contiguous non-empty subarray within an array A of length N.
##Problem Constraints
#1 <= N <= 1e6
#-1000 <= A[i] <= 1000
#
#Input Format
#The first and the only argument contains an integer array, A.
#
#Output Format
#Return an integer representing the maximum possible sum of the contiguous subarray.
#
#Example Input
#
#Input 1:
# A = [1, 2, 3, 4, -10] 
#Input 2:
# A = [-2, 1, -3, 4, -1, 2, 1, -5, 4] 
#
#Example Output
#Output 1:
# 10 
#Output 2:
# 6 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        # array elements can be positive or negative
        # if all array elemes are positive then the sum of entire array/
        # if all array elements are negative then the highest negative number
        # if there is a mix of pos and negative elem then use kadanes algo
        # Brute Force - add all ements from 0 to n-1
        # then add all elements from 1 to n-1
        # then add all elements from 2 to n-1
        # after each addition compare the sum to the max  
        # O(Nsquare) solution
        # gsum = -float('inf')
        # for i in range(len(A)):
        #     tempsum = 0
        #     for j in range(i,len(A)):
        #         tempsum += A[j]
        #         if gsum < tempsum:
        #             gsum = tempsum
        # return gsum
        #using kadanes algo O(N) solution
        # whenever a negative sum is encountered reset sum to 0, only a single iteration of entire array is needed
        gsum = -float('inf')
        tempsum = 0
        for i in A:
            tempsum += i
            if tempsum>gsum:
                gsum = tempsum
            if tempsum<0:
                tempsum=0
        return gsum


s = Solution()
print(s.maxSubArray([1,2,3,4,5,6,7,-5]))
                        
