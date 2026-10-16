class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1] * len(nums)
        output = []
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i + 1] * right[i + 1]

        for i in range(len(nums)):
            if i == 0:
                continue
            left.append(nums[i-1] * left[i-1])

        for i in range(len(nums)):
            output.append(left[i] * right[i])

        return output