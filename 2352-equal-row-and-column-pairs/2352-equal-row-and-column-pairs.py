class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        dic_h = {}
        dic_v = {}
        for i in range(len(grid)):
            tem = ''
            for j in range(len(grid[0])):
                tem += str(grid[i][j]) + '_'
            if tem in dic_h:
                dic_h[tem] += 1
            else:
                dic_h[tem] = 1
        
        for i in range(len(grid[0])):
            tem = ''
            for j in range(len(grid)):
                tem += str(grid[j][i]) + '_'
            if tem in dic_v:
                dic_v[tem] += 1
            else:
                dic_v[tem] = 1

        count = 0
        for i in dic_h:
            if i in dic_v:
                count += dic_h[i] * dic_v[i]
        return count
        
    
        
