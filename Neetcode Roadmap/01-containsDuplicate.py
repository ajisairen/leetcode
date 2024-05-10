class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # convert nums to a set and compare the lengths
        return len(set(nums)) != len(nums)
