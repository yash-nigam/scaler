Algorithm: Merge Overlapping Intervals1. 

Problem Statement : 
Given an array of intervals, merge all overlapping intervals and return an array of non-overlapping intervals 
that cover all the intervals in the input.

Example:Input: [[1, 3], [2, 6], [8, 10], [15, 18]]
Output: [[1, 6], [8, 10], [15, 18]]

Note: [1, 3] and [2, 6] overlap, so they merge into [1, 6].

Conditions for Overlap
To determine if two intervals $A(s_1, e_1)$ and $B(s_2, e_2)$ overlap, we look at the start and end points.
Non-Overlapping Conditions
Two intervals do not overlap if:The second interval starts after the first one ends: $s_2 > e_1$
The first interval starts after the second one ends: $s_1 > e_2$

Logic: If $(s_2 > e_1 \text{ OR } s_1 > e_2)$, 
then there is no overlap.

Overlapping Condition (Simplified for Sorted Arrays)
If the intervals are sorted by their start times, we only need to check:
Overlap exists if: $s_2 \leq e_1$Merged Interval: $(\min(s_1, s_2), \max(e_1, e_2))$3. 
Algorithmic Logic (Optimal Approach)
Step 1: SortingSort the array in ascending order based on the start times. 
This ensures that potentially overlapping intervals are adjacent.
Step 2: Iteration & Merging
    Initialize the current interval $(s, e)$ with the first interval in the array.
    Iterate through the remaining intervals $(ns, ne)$:If Overlap ($ns \leq e$):Update the current end: $e = \max(e, ne)$If No Overlap:Push the completed current interval $[s, e]$ to the answer array.Reset the current interval to the new one: $s = ns, e = ne$.After the loop: Append the last remaining interval $[s, e]$ to the answer array.4. Dry Run TableTracing the input: [[0, 2], [1, 4], [5, 6], [6, 8], [7, 10], [8, 9], [12, 14]]#Current Interval (s,e)Next Interval (ns,ne)Overlap? (ns≤e)Action / New Range1[0, 2][1, 4]$1 \leq 2$ (Yes)Merge $\to [0, 4]$2[0, 4][5, 6]$5 \leq 4$ (No)Add [0, 4] to Ans; New $(s, e) = [5, 6]$3[5, 6][6, 8]$6 \leq 6$ (Yes)Merge $\to [5, 8]$4[5, 8][7, 10]$7 \leq 8$ (Yes)Merge $\to [5, 10]$5[5, 10][8, 9]$8 \leq 10$ (Yes)Merge $\to [5, 10]$ (since $\max(10, 9)=10$)6[5, 10][12, 14]$12 \leq 10$ (No)

def merge_intervals(input_array):
    print(input_array)
    ans_array = []
    s = input_array[0][0]
    e = input_array[0][1]   
    for i in range(1,len(input_array)):
        ns = input_array[i][0]
        ne = input_array[i][1]
        if ns <= e:
            s = min(s,ns)
            e = max(e,ne)
        else:
            ans_array.append([s,e])
            s = ns
            e = ne
    ans_array.append([s,e])
    print(ans_array)


input_array=[[0,2],[1,4],[5,6],[6,8],[7,10],[8,9],[12,14]]
merge_intervals(input_array)

print("Hello")
