# Problem Description
# You will be given an integer n. You need to return the count of prime numbers less than or equal to n.


# Problem Constraints
# 0 <= n <= 10^3


# Input Format
# Single input parameter n in function.


# Output Format
# Return the count of prime numbers less than or equal to n.


# Example Input
# Input 1:
# 19
# Input 2:
# 1


# Example Output
# Output 1:
# 8
# Output 2:
# 0


# Example Explanation
# Explanation 1:
# Primes <= 19 are 2, 3, 5, 7, 11, 13, 17, 19
# Explanation 2:
# There are no primes <= 1
class Solution:
    # @param A : integer
    # @return an integer
    def num_prime_check(self,A):
        if A==1:
            return False
        for i in range(2,A):
            if A%i==0:
                return False
        return True

    def solve(self, A):
        prime_count=0
        for i in range(1,A+1):
            if self.num_prime_check(i)==True:
                prime_count+=1
        return prime_count
