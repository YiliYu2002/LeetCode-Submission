class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        nums, res = [], []
        for i in obstacles:
            pos = bisect_right(nums,i)
            if pos == len(nums):
                nums.append(i)
            else:
                nums[pos] = i
            res.append(pos + 1)
            
        return res