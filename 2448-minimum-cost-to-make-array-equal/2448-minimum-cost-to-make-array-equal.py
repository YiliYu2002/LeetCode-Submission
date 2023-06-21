class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def calc(n):
            cos = 0
            for i, j in enumerate(nums):
                cos += abs(j - n) * cost[i]
            return cos
        
        mi, ma = min(nums), max(nums) + 1
        mid = (mi + ma) // 2

        while mi < ma:
            if calc(mid) < calc(mid + 1):
                ma = mid
            else:
                mi = mid + 1
            mid = (mi + ma) // 2
        return calc(mi)
