class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        num = 1
        for i in range(len(digits)-1, -1, -1):
            tem = num + digits[i]
            if tem >= 10:
                res.append(tem - 10)
                num = 1
            else:
                res.append(tem)
                num = 0
        if num == 1:
            res.append(num)
        return res[::-1]
            
