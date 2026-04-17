# def twosum(arr: list[int], target) -> []:
#     #print(len(arr))
#     for i in range(len(arr)):
#         for j in range(i+1, len(arr)):
#             print(i,arr[i],j, arr[j])
#             if arr[i]+arr[j] == target:
#                 return[i,j]
#     return [-1,-1]

# print(twosum([1,5,2,7,4,17,25,9,6,19,35,27],14))

# def twosumhashmap(arr: list[int], target)-> []:
#     hm ={}
#     for i in range(0,len(arr)):
#         complement = target - arr[i]
#         if complement in hm:
#             return(i,hm[complement])
#         else:
#             hm[arr[i]] = i
#         print(hm)
#     return([-1,-1])
# print(twosumhashmap([1,5,2,7,4,17,25,9,6,19,35,27],14))

# def twosumtwopointer(arr: list[int], target):
#     arr2 = []
#     for i in range(0,len(arr)):
#         arr2.append([arr[i],i])
#     print(arr2)
#     arr2.sort(key=lambda x: x[0])
#     print(arr2)
#     l=0
#     r=len(arr)-1
#     while l < r:
#         if arr2[l][0] + arr2[r][0] == target:
#             return[arr2[l][1] ,arr2[r][1]]
#         elif arr2[l][0] + arr2[r][0] < target:
#             l += 1
#         else:
#             r -= 1
#     return [-1,-1]


# print(twosumtwopointer([1,5,2,7,4,17,25,9,6,19,35,27],14))


# def mergeinterval(arr: list[[int]]):
#     print(arr)
#     arr.sort(key=lambda x: x[0])
#     print(arr)
#     s=arr[0][0]
#     e=arr[0][1]
#     ansarr =[]
#     for i in range(1,len(arr)):
#         print(i)
#         if arr[i][0] <= e:
#             s=min(s,arr[i][0])
#             e=max(e,arr[i][1])
#             print(s,e)
#         else:
#             ansarr.append([s,e])
#             s=arr[i][0]
#             e=arr[i][1]
#         print(ansarr)            
#     ansarr.append([s,e])
#     print(ansarr) 


# print(mergeinterval([[0, 2], [1, 4], [5, 6], [6, 8], [12, 14],[7, 10], [8, 9] ]))
# print(mergeinterval([[0, 4], [2, 9], [13, 17]]))



def rainwatertrap(heights: list[int]):
    print(heights)
    maxlheights = []
    maxrheights = [0] * len(heights)
    maxl=0
    maxr=0
    res = 0
    for i in range(len(heights)):
        maxlheights.append(maxl)
        if heights[i] > maxl:
            maxl=heights[i]
    for i in range(len(heights)-1,-1,-1):
        maxrheights[i]=maxr
        if heights[i] > maxr:
            maxr=heights[i]
    print(heights)
    print(maxlheights)
    print(maxrheights)
    for i in range(len(heights)):
        x = min(maxlheights[i],maxrheights[i])-heights[i]  
        res += x if x > 0 else 0
        print(res)


print(rainwatertrap([0,1,0,2,1,0,1,3,2,1,2,1]))