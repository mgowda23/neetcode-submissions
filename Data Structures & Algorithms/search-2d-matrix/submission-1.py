class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows-1

        while left <= right :
            mid = (left+right) // 2
            low = matrix[mid][0]
            high = matrix[mid][-1]

            if target < low :
                right = mid -1
            elif target > high :
                left = mid +1
            else:
                break
        
        if not (left <= right):
            return False
        mid = (left + right) //2
        l,r =0, cols -1
        while l <= r:
            m = (l+r) //2
            if target == matrix[mid][m]:
                return True
            elif target < matrix[mid][m]:
                r = m-1
            else: l = m+1
        return False