class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        result = []
        r, c = 0, 0
        result.append(mat[r][c])
        direction = 0
        m = len(mat)
        n = len(mat[0])

        while True:
            if direction == 0:
                if r - 1 >= 0 and c + 1 < n:
                    r -= 1
                    c += 1
                    result.append(mat[r][c])
                else:
                    if c + 1 < n:
                        c += 1
                        result.append(mat[r][c])
                    elif r + 1 < m:
                        r += 1
                        result.append(mat[r][c])
                    else:
                        break
                    direction = 1
            else:
                if r + 1 < m and c - 1 >= 0:
                    r += 1
                    c -= 1
                    result.append(mat[r][c])
                else:
                    if r + 1 < m:
                        r += 1
                        result.append(mat[r][c])
                    elif c + 1 < n:
                        c += 1
                        result.append(mat[r][c])
                    else:
                        break
                    direction = 0

        return result