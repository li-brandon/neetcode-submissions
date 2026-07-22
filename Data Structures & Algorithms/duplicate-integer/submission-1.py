class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False

        temp = set(nums)
        return True if len(temp) != len(nums) else False