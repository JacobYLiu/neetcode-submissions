class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        if len(s) != len(nums): 
            return True
        print(s)
        return False