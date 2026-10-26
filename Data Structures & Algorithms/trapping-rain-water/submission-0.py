class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        suffix = []
        output = []
        for i in range(len(height)):
            if i == 0:
                prefix.append(height[i])
            else:
                if height[i] >= prefix[i-1]:
                    prefix.append(height[i])
                else:
                    prefix.append(prefix[i-1])


        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                suffix.append(height[i])
            else:
                if height[i] >= suffix[(len(height)-1)-i-1]:
                    suffix.append(height[i])
                else:
                    suffix.append(suffix[(len(height)-1)-i-1])
        suffix = suffix[::-1]


        for i in range(len(height)):
            output.append(min(prefix[i],suffix[i])-height[i])       
        return sum(output)