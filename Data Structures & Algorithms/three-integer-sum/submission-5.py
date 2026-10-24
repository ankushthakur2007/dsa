class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        c = sorted(nums)
        output = []

        for i in range(len(c)):
            l = i+1
            r = len(c) - 1
            while r > l:
                if c[i] +c[l] + c[r] == 0:
                    if [c[i],c[l],c[r]] not in output:
                        output.append([c[i],c[l],c[r]])
                    l+=1
                    r-=1    

                elif c[i] +c[l] + c[r] > 0:
                    r -=1
                elif c[i] +c[l] + c[r] < 0:
                    l +=1
                
        return output
