class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for a in strs:
            s += str(len(a))+"#"+a

        return s
    def decode(self, s: str) -> List[str]:
        start = 0 
        output =[]
        while start < len(s):
            i = s.find("#",start)
            length = int(s[start:i])

            word = s[i+1:i+1+length]
            output.append(word)
            start = i+1+length
        return output