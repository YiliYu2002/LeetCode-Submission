class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = len(nums) // 2 + 1
        for i in nums:
            if i == target:
                count -= 1
        if count <= 0:
            return True
        return False