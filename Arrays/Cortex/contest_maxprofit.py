# contest
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        if not A:
            return 0
        lowestA = []
        lowestA.append(0)
        lowest=A[0]
        for i in range(1,len(A)):
            lowestA.append(lowest)
            lowest = min(lowest, A[i])
        #return lowestA
        maxval = 0
        if len(A) > 1:
            for i in range(1,len(A)):
                maxval = max(maxval, A[i]-lowestA[i])
        return maxval
