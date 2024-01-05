from collections import deque
from queue import Queue
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        fresh_oranges, minutes = 0, 0
        rotten_queue = Queue()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    rotten_queue.put([i, j])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while not rotten_queue.empty() and fresh_oranges > 0:
            for _ in range(rotten_queue.qsize()):
                i, j = rotten_queue.get()

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_oranges -= 1
                        rotten_queue.put([ni, nj])

            minutes += 1

        return minutes if fresh_oranges == 0 else -1


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        fresh_oranges, minutes = 0, 0
        rotten_queue = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_oranges += 1
                if grid[i][j] == 2:
                    rotten_queue.append([i, j])
        directions = [[0, 1], [0, -1], [1, -0], [-1, 0]]
        while rotten_queue and fresh_oranges > 0:
            for i in range(len(rotten_queue)):
                i, j = rotten_queue.popleft()

                for di, dj in directions:
                    ni, nj = i + di, j+dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh_oranges -= 1
                        rotten_queue.append([ni, nj])
            minutes += 1

        return minutes if fresh_oranges == 0 else -1
