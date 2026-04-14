# this is the simpler solution which consume more memory
# the water present at any given location can be determined by the following rule
# minof(maxL, maxR) - height(i)
# so we need to prepare in advance all minimum and max left and rights for all values so 2 differ arrays are required

class Solution:
    def rainwatertrap(self, heights: list[int]) -> int:
        maxlArray = []
        maxrArray = [0] * len(heights) # as we need to have the righmost array elemnt available
        maxl = 0 #left of 0th position is not defined so it is 0
        maxR = 0 #right of nth position is not defined so 0
        res = 0
        for i in range(0,len(heights)):
            maxlArray.append(maxl)
            if maxl < heights[i]:
                maxl = heights[i]         
            print(i, heights[i], maxl, maxlArray[i])
        for i in range(len(heights)-1,0,-1):
            maxrArray[i]=maxR
            if maxR < heights[i]:
                maxR = heights[i]         
            print(i, heights[i], maxR, maxrArray[i])
        for i in range(len(heights)):
            x= min(maxlArray[i],maxrArray[i])-heights[i]
            res += x if x >= 0 else 0
            print(res)


s= Solution()
s.rainwatertrap([0,1,0,2,1,0,1,3,2,1,2,1])