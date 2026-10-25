class Solution:
    def maxArea(self, heights: List[int]) -> int:
        output = []
        l = 0 
        r = len(heights)-1
        while l < r:
            if heights[l] > heights[r]:
                output.append(heights[r]*(r-l))
                r -=1
            elif heights[l]<heights[r]:
                output.append(heights[l]*(r-l))
                l +=1
            elif heights[l]==heights[r]:
                output.append(heights[l]*(r-l))
                l +=1
                continue
        return max(output)  