class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        array_length = len(nums) + 1
        for i in range(0, array_length):
            if not i in nums:
                return i