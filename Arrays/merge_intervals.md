The Markdown output I provided above is already formatted for you, but here is a clean, copy-pasteable version structured specifically as a technical study note.

---

# Study Notes: Merge Overlapping Intervals

## 1. Problem Definition
Given a 2D array of intervals, merge all overlapping intervals and return an array of the resulting non-overlapping intervals.

**Example Input:** `[[1, 3], [2, 6], [8, 10], [15, 18]]`
**Example Output:** `[[1, 6], [8, 10], [15, 18]]`

---

## 2. Overlap Logic
To efficiently check for overlaps, we look at the relationship between the **End** of the current interval ($e_1$) and the **Start** of the next interval ($s_2$).

### Conditions for Non-Overlap
Two intervals do not overlap if there is "daylight" between them:
* **Condition 1:** $s_2 > e_1$ (Second starts after first ends)
* **Condition 2:** $s_1 > e_2$ (First starts after second ends)

### Condition for Overlap (Sorted)
If the array is sorted by start times, we only need to check one condition:
* **Overlap exists if:** $s_2 \leq e_1$
* **Merged Result:** $(\min(s_1, s_2), \max(e_1, e_2))$

---

## 3. Algorithmic Approach (Brute Force vs. Optimized)

* **Brute Force:** Compare every interval with every other interval. This is inefficient ($O(n^2)$).
* **Optimized Logic:** By **sorting** the intervals by start time, all potentially overlapping intervals become neighbors. This allows us to solve the problem in a single pass ($O(n \log n)$ due to sorting).

### Step-by-Step Process:
1.  **Sort** the array based on the start points.
2.  **Initialize** variables `s` and `e` with the first interval's values.
3.  **Iterate** through the rest of the array:
    * If the next start point $ns \leq e$, update $e = \max(e, ne)$.
    * Otherwise, the current interval is finished. **Append** `[s, e]` to the result and reset `s` and `e` to the current interval's values.
4.  **Finalize:** Don't forget to append the very last interval after the loop finishes.

---

## 4. Dry Run Trace
**Input:** `[[0, 2], [1, 4], [5, 6], [6, 8], [7, 10], [8, 9], [12, 14]]`

| Step | Current $(s, e)$ | Next $(ns, ne)$ | Overlap? | Action |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `[0, 2]` | `[1, 4]` | Yes ($1 \leq 2$) | Merge: $e = \max(2, 4) \to 4$ |
| 2 | `[0, 4]` | `[5, 6]` | **No** ($5 > 4$) | **Push `[0, 4]`**; New $(s, e) = [5, 6]$ |
| 3 | `[5, 6]` | `[6, 8]` | Yes ($6 \leq 6$) | Merge: $e = \max(6, 8) \to 8$ |
| 4 | `[5, 8]` | `[7, 10]` | Yes ($7 \leq 8$) | Merge: $e = \max(8, 10) \to 10$ |
| 5 | `[5, 10]` | `[8, 9]` | Yes ($8 \leq 10$) | Merge: $e = \max(10, 9) \to 10$ |
| 6 | `[5, 10]` | `[12, 14]` | **No** ($12 > 10$) | **Push `[5, 10]`**; New $(s, e) = [12, 14]$ |
| End | — | — | — | **Push `[12, 14]`** |

**Final Answer:** `[[0, 4], [5, 10], [12, 14]]`

---

## 5. Implementation (Python Logic)
```python
def merge(intervals):
    if not intervals: return []
    
    # Sort by start point
    intervals.sort(key=lambda x: x[0])
    
    ans_array = []
    s = intervals[0][0]
    e = intervals[0][1]
    
    for i in range(1, len(intervals)):
        ns, ne = intervals[i]
        
        if ns <= e: # Overlap
            e = max(e, ne)
        else: # No overlap
            ans_array.append([s, e])
            s, e = ns, ne
            
    ans_array.append([s, e]) # Add the final interval
    return ans_array
```