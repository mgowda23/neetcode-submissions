class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        res = [[float('inf')] * (n+1) for _ in range(m+1)]

        for j in range(n+1):
            res[m][j] = n-j
        for i in range(m+1):
            res[i][n] = m-i

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word1[i] == word2[j]:
                    res[i][j] = res[i+1][j+1]
                else:
                    res[i][j] = 1 + min(
                        res[i+1][j],
                        res[i][j+1],
                        res[i+1][j+1]
                    )
        return res[0][0]