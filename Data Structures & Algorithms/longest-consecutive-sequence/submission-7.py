class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        b = sorted(a)
        current = set()
        longest = set()

        if len(b) == 1:
            longest.add(1)
        elif len(b) == 0:
            return len(longest)
        
        elif len(b) > 1:
            for i in range(len(b)-1):
                if b[i]+1 == b[i+1]:
                    current.update([b[i],b[i+1]])
                else:
                    if len(current) > len(longest):
                        longest = current.copy()
                        current = set()

                    else :
                        current = set()
            if longest == set():
                longest.add(1)

        if len(current) > len(longest):
            longest = current.copy()

        return len(longest)
