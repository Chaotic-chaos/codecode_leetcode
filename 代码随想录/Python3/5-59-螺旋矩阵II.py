# -*- coding: utf-8 -*-
'''
Project:       ~/projects/leetcode/代码随想录/Python3
File Name:     5-59-螺旋矩阵II.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2023/04/09
Software:      Vscode
'''

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res_matrix = [[1]*n for _ in range(n)]
        start_x = 0
        start_y = 0

        loop = n//2
        mid = n//2  # if the n is odd number, need to deal with the middle slot

        count = 1

        for offset in range(1, loop+1):
            for i in range(start_y, n-offset):
                # from left to right
                res_matrix[start_x][i] = count
                count += 1

            for i in range(start_x, n-offset):
                # from top to bottom
                res_matrix[i][n-offset] = count
                count += 1

            for i in range(n-offset, start_y, -1):
                # from right to left
                res_matrix[n-offset][i] = count
                count += 1

            for i in range(n-offset, start_x, -1):
                # from bottom to top
                res_matrix[i][start_y] = count
                count += 1

            start_x += 1
            start_y += 1

        if n % 2 != 0:
            res_matrix[mid][mid] = count

        return res_matrix


if __name__ == '__main__':
    n = 3

    solution = Solution()

    print(solution.generateMatrix(n=n))
