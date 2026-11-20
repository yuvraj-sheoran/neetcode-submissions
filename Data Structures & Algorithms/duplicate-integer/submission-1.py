class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupli = set()
        for i in range(len(nums)):
            if nums[i] in dupli:
                return True
            else:
                dupli.add(nums[i])
        return False
            
        