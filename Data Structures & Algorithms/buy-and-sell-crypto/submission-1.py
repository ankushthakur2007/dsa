class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = len(prices)-1
        output = []
        prefix = []

        for i in range(len(prices)):
                    if i == 0:
                        prefix.append(prices[i])
                    else:
                        if prices[i] <= prefix[i-1]:
                            prefix.append(prices[i])
                        else:
                            prefix.append(prefix[i-1])

        for i in range(len(prices)):
            if prices[i] > prefix[i]:
                output.append(prices[i] - prefix[i])
            else:
                continue
        if len(output) == 0:
            return 0
        else:
            return max(output)