
---

# 2 Sum Problem

**Problem Statement:**
Given an array of integers `arr[]` and an integer `target`, check if a pair exists in that array which sums up to the target.

* **Return 1:** Return "Yes" if such two numbers exist, else "No".
* **Return 2:** Return indices of the two integers. Otherwise, return `[-1, -1]`.

**Example:**
* **Input:** $N = 5$, $arr = \{2, 6, 5, 8, 11\}$, $target = 14$
* **Logic:** $8 + 6 = 14 \rightarrow arr[1] + arr[3] = 14$
* **Output:** Yes / `[1, 3]`

---

## Option 1: Brute Force Solution
Compare/add all elements to each other to find the target. Start from the $0^{th}$ element, add the $1^{st}$ element, and check if it equals the target. If not, add $0^{th}$ and $2^{nd}$, continuing until $N$. If no match is found for the $0^{th}$ index, increment the base index to $1^{st}$ and check $1^{st} + 2^{nd}$, $1^{st} + 3^{rd}$, etc.

### Iteration Analysis (For $N=7$)
We need two nested for loops. If the target is never found:
* **$0^{th}$ element:** Iterates from index $1$ to $6$ (**6 iterations**)
* **$1^{st}$ element:** Iterates from index $2$ to $6$ (**5 iterations**)
* **$2^{nd}$ element:** Iterates from $3$ to $6$ (**4 iterations**)
* **$3^{rd}$ element:** Iterates from $4$ to $6$ (**3 iterations**)
* **$4^{th}$ element:** Iterates from $5$ to $6$ (**2 iterations**)
* **$5^{th}$ element:** Iterates from index $6$ (**1 iteration**)

**Total Iterations:** $6 + 5 + 4 + 3 + 2 + 1 = 21$
**Formula:** $\frac{n(n-1)}{2} \rightarrow \frac{7(7-1)}{2} = \frac{42}{2} = 21$ iterations.


## Time Complexity: 
O(n^2)

The time complexity is Quadratic.

Total iterations are n(n-1)/2 becoz we have nested loop 

### In Big O notation
we drop constants and lower-order terms, leaving us with $O(n^2)$.

Performance Impact: As your input array grows, the time it takes to finish grows exponentially. If the array size doubles, *the work required quadruples.*

---

## Option 2: Use Hash Map

### what is a hashmap in python
In Python, a HashMap is implemented through the built-in dict (dictionary) data type. It is a collection that stores data in key-value pairs, allowing you to retrieve a value almost instantly if you know its corresponding key.

**Logic:**
1. For every $i$, check if $(Target - arr[i])$ exists in the HashMap.
-  the difference we are looking for 
2. If it exists, return "Yes" or the indices.
3. If it doesn't exist, put the current element $arr[i]$ as the key and its index $i$ as the value into the HashMap.
4. this is because we have to return the index if the sum is found
(key,value)=($i$, $arr[i]$)
- so why do we insert it in the hashmap
  - we want two numbers whose sum is equal to the target
  - one of the numbers is at arr[i], the other number is Target-arr[i]
  - now if this differnece is present in the array the we have found solution
  - but how to find the difference in the array should we do a brute force loop again scanning all elements to find solution
  - but that is exactly what we did in the previous approach
  - so what we do is we record the previous value of array in an hashmap along with their index,
  - technically we can also use the in operator of python
  because in future iterations if the difference between target and any number is present in the hashmap then we have found the solution

### Code Implementation
```python
def sum_exist(arr, target):
    h = {} # HashMap
    for i in range(0, len(arr)):
        complement = target - arr[i]
        if complement in h:
            # Variant 1: return "Yes"
            # Variant 2: return [h[complement], i]
            return "Yes" 
        else:
            h[arr[i]] = i
    return "No"
```
### code returning the indexes of the two elements
```python
def sum_exist(arr, target):
    h = {} # HashMap
    for i in range(0, len(arr)):
        complement = target - arr[i]
        if complement in h:
            # Variant 1: return "Yes"
            # Variant 2: return [h[complement], i]
            return [i,h[complement]]
        else:
            h[arr[i]] = i
    return [-1,-1]
```
### Time Complexity: $O(n)$
This is Linear Time complexity 
- only one loop that iterates through the list once.
- looking up a key (if complement in hm) takes, on average, $O(1)$ time.
- Total Operations: Since you do one pass and each lookup is nearly instantaneous, the time taken grows in direct proportion to the size of the array. Linear
- If the array size doubles, the time taken roughly doubles (instead of quadrupling).

###Space Complexity: $O(n)$
This is Linear Space.ems in your input list, the more space the dictionary takes up in RAM.
---

## Option 3: Two-Pointer Approach on a Sorted Array
This method works by sorting the array and using two pointers
- First pointer starting from 0th index from left to right 
- Second pointer starting from rightmost n-1 index to left
- During sorting the places of values in the array changes, however to return the indices of the original array those places must be preserved


**Logic:**
1. Create a 2D array to store the number and its original index.
2. Sort the array based on the numbers.
    - how to do this in python 
3. Place `l` (left pointer) at the start and `r` (right pointer) at the end.
4. While `l < r`:
    * If `sum == target`: Return indices.
    * If `sum > target`: Move `r` left (`r--`) to decrease the sum.
    * If `sum < target`: Move `l` right (`l++`) to increase the sum.


### Code Implementation
```python
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
```

### Complexity Analysis
* **Time Complexity (T.C.):** $O(N \log N)$ due to sorting. The while loop itself is $O(N)$.
* **Space Complexity (S.C.):** $O(N)$ because we store $N$ variables (and their indices) in a new array.

---

Would you like to see how the space complexity changes if we don't need to return the indices?