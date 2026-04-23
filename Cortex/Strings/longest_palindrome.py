# The question is to find out the longest palindrome in a string the palindrome can occur anywhere
# The brute force solution is to generate all combination of substrings i,e, start with 0th char, then oth and 1st till n, then start with 2.nd char then till n
# thsi alone would reauire a n sq tc as there would be two for loops
# additionally once we have the substrings we need to verify them if they are palindrom or not so we would have to have two pointer starting from left and right # that would again require a loop

# another option is to start from the first pistion of string and fan out to left and right side , expend to left and right sides
# for an odd lenght palindrom the all the characters left and right to the central character should be equal aba cvfvc
# for an even lenght palindrm the two central chars must be same and after that it would be same logic as the odd one abba abcddcba
# so for even length take 2 centers i and i +1 go from i+1 to n and go from i to 0
# if i is the 0th index then we cant go left it means i itself is palindrome
# if i is at 1st index then at max we can go to 0 and we can go to 2
# 0 and 2 could be same or different
# what if the input is aab. here we need to make sure that aa is counted as substring
# aa is an even string so it shouldbe treated with even logic
# aab is odd length 
# we should create antoher function which will simply use the center method to find if strings are palin or not


# there will beonly one loop from 0 to n
# for every index the expand method will be called twice
# once for even and once for odd number of items in array
# because same method cannot deal with even and odd length strings

#also we dont know at which index the string will be an even palindrome or odd palindrome
def findpalindrome(s):
    start,end = 0,0
    for i in range(len(s)):
        # in advance we do not know that whether a string will be odd or even palindrime
        # so for each index we call both even and odd methods
        # for odd - the left and right pointers will be -1 and +1 of i as i iteself is center
        print("odd Start")
        len_odd = expand(s, i-1,i+1)
        # length of substring if found palindrome is returned
        # based on thsi we need to caluclate start and ending points
        # for even- the middle two would be the center hence it would be i and next
        print("even start")
        len_even = expand(s,i,i+1)
        max_len = max(len_even,len_odd)
        print(max_len)
        # check if a new max has been found
        if max_len > end-start+1:
            # start index fo length of max_len from position i is 
            # from the current pointer go left max_len-1/2 positions
            start = i -(max_len-1)//2
            # end is go to right max_len/2 positions
            end = i +(max_len//2)
        print("longest palindrome = ",s[start:end+1])
    return s[start:end]

def expand(s,l,r):
    print("expand start withl=",l,"and r=",r)
    while l >=0 and r <len(s) and s[l] == s[r]:
            l -=1 
            r += 1
    print("expand end")
    #here length is being returned
    return r-l-1

    
findpalindrome("qaqabcddcbaabc")

