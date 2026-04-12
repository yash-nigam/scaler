# brute force approach
def twosum(arr,target)->list:
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j] == target:
                return [i,j]
    return [-1,-1]
print(twosum([2,7,11,15],45))
# in this approach the time complexity will be o(n^2) and space complexity will be o(1) 
# the total iterations with the two for loops wwill be n*(n-1)/2 so if there are 4 elements in array then total itreations will be 4*3/2 = 6 iterations 
# but 6 is not the total number of iterations because we are also doing addition and comparison in each iteration so the total number of operations will be 6*2 = 12 operations     
#but the time complexity is n sqaure so in this case it is 6 square which is 36 operations but we are doing 12 operations so the time complexity is o(n^2) and space complexity is o(1) because we are not using any extra space to store the result we are just returning the indices of the elements that add up to the target.   

# now an optimized approach using hash map
def twosumhashmap(arr,target)->list:
    hash_map = {}
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[arr[i]] = i
    return [-1,-1]
print(twosum([2,7,11,15],22))


# another approach using the two pointer method on an sorted arry
# Create a 2D array to store the number and its original index.
# Sort the 2d array based on the first element.
# how to do this in python
# Place l (left pointer) at the start and r (right pointer) at the end.
# While l < r:
#If sum == target: Return indices.
#If sum > target: Move r left (r--) to decrease the sum.
#If sum < target: Move l right (l++) to increase the sum.
#

# 2 pointer method on an sorted array
def twosumtwopointer(arr,target)->list:
    temp = []
    for i in range(len(arr)):
        temp.append([arr[i],i])
    
    # Sorts nums directly based on the element at index 0
    temp.sort(key=lambda x: x[0])
    #lambda x: x[0] means "Take the sub-list x and look only at its first element (index 0) for the comparison logic
        
    l = 0
    r= len(arr)-1
    while l < r:
        if temp[l][0] + temp[r][0] == target:
            return(temp[l][1], temp[r][1])
        elif temp[l][0] + temp[r][0] > target:
            r-=1
        else: 
            l+=1
    return [-1,-1]
print(twosumtwopointer([2,7,11,15],22))