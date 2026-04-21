# a string has a sentence separated by spaces
# the output should be the last word first, then second last separated by space and so on till the first
# the simples solutino is 
    # to use python inbuilt utilities to break string using space as delimiter which will give as array
    # form a new string by iterating from rightmost araay item to left
# The better solution is
    # start from the rightmost character keep counter l and r here
    # move left until space is found 
    # when space is found extract the characters between l and  r counter and put to new string
    # put l and r at one index beind space

class Solution:
    def solve(self, A):
        a_length= len(A)
        l,r = a_length-1,a_length-1
        while l >= 0:
            while A[l] != " " and l >=0:
 #               print(l,r, A[l])
                l -= 1
            print(A[l+1:r+1])
            while A[l]  == " ":
                l = l-1
            r = l


s = Solution()
print(s.solve("a quick    brown fox     jumed over the  lazy dog"))
