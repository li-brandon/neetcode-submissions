class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        unique_nums = []
        for i in nums:
            if i != val:
                unique_nums.append(i)

        nums[:] = unique_nums
        
        return len(unique_nums)