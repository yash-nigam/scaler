# The question is to find out the longest palindrome in a string the palindrome can occur anywhere
# The brute force solution is to generate all combination of substrings i,e, start with 0th char, then oth and 1st till n, then start with 2.nd char then till n
# thsi alone would reauire a n sq tc as there would be two for loops
# additionally once we have the substrings we need to verify them if they are palindrom or not so we would have to have two pointer starting from left and right # that would again require a loop

# another option is to start from the first pistion of string and fan out to left and right side , expend to left and right sides
# for an odd lenght palindrom the all the characters left and right to the central character should be equal aba cvfvc
# for an even lenght palindrm the two central chars must be same and after that it would be same logic as the odd one abba abcddcba

