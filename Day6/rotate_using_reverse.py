class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def rev(self,A,l,r):
        while(l<r):
            temp=A[r]
            A[r]=A[l]
            A[l]=temp
            l+=1
            r-=1
        return A

    def rotate_via_rev(self,A,k):
        A=self.rev(A,0, len(A)-1)
        A=self.rev(A,0,k-1)
        A=self.rev(A,k,len(A)-1)
        return A

    def solve(self, A, B):
        if(len(A)<B):
            B=B%len(A)
            #print("B=",B)
        if B>0:    
            self.rotate_via_rev(A,B)
        return A
