import sys
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        mx=-sys.maxsize-1
        mn=sys.maxsize
        for i in range(0,len(A)):
            if A[i]>mx:
                mx=A[i]
            if A[i]<mn:
                mn=A[i]
        return mx+mn

