# write a program to find the long prefix in a list of strings in an array
# here the brute force approach - somehow we will have to  compare every string with every other string and then find the longest prefix found
# other way is to firt sort the strings in array in lexicographical order i.e. alphabetical order
# once they are storted the leftmost string will have the least amount of chars
# hence the prefix should be not more than the smallest element in the array
# similarly the last element should have the largest amount of characters
# so we will start comparing the first and last string character by character
# starting from left index if character matches then i+=1 , and if at a point the characters do not match then we have foudn the largest prefix
# there cannot be anu other string larger than this because we have already sorted
# the strings with the most similar prefixes should be together and the least at the last
# hence if we compare the first and last we get the largest possible commn prefix which is the starting no no of same characters in them

class Solution:
    def solve(self, A):
        # first sort the array of strings
        A.sort()
        # get first and last indexes
        start = 0
        end = len(A)-1
        # compare the characters of first and last strings one at a time
        # increment counter if match found otherwise return 
        # comparison should only be done until the length of smaller string
        prefix_count=0
        for i in range(0, min(len(A[start]),len(A[end]))):
            if A[start][i] == A[end][i]:
                prefix_count +=1
            else:
                break
        return A[start][0:prefix_count]

s = Solution()
print(s.solve(["flower","flow","flowing"]))
