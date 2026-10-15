class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums2  = Counter(nums)

        group = nums2.most_common(k)
        only_numbers = []

        for i in range(0,k):
            only_numbers.append(group[i][0])


        return only_numbers