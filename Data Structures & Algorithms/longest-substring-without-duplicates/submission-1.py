class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = {}
        l = 0
        r = 0
        max_number = 0

        while r <= len(s) -1 :
            if s[r] in a:
                l = max(a[s[r]] + 1, l)

            a[s[r]] = r
            max_number = max(max_number, r - l + 1)
            r += 1
        return max_number

