class Solution:

    # You cannot create a new list or set
    # You must modify the existing nums array itself
    # The function must return k, the number of unique elements

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        i = 1 # position for next unique element
        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i