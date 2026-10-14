class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # more genius approach 
        a = Counter(s)
        b = Counter(t)
        
        return a==b


    
            