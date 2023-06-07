class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        A, B, C = bin(a)[2:], bin(b)[2:], bin(c)[2:]
        ml = max(len(A), len(B), len(C))
        A = '0' * (ml - len(A)) + A
        B = '0' * (ml - len(B)) + B
        C = '0' * (ml - len(C)) + C
        dic = {'000': 0, '010': 1, '100': 1, '110':2,
        '001': 1, '011': 0, '101': 0, '111': 0}
        count = 0
        for i in range(ml):
            count += dic[A[i]+B[i]+C[i]]
        return count


