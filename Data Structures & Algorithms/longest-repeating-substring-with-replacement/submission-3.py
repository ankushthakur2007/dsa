class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        max_string = 0
        count = Counter()
        max_freq = 0
        while r <= len(s)-1:
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            max_string = max(max_string, r - l + 1)
            r += 1

        return max_string