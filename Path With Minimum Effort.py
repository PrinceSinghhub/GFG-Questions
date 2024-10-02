from typing import List
from queue import PriorityQueue


class Solution:
    def MinimumEffort(self, rows: int, columns: int, heights: List[List[int]]) -> int:
        effort = [[float('inf')] * columns for _ in range(rows)]

        pq = PriorityQueue()
        pq.put((0, 0, 0))  # (row, col, effort)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while not pq.empty():
            curr = pq.get()
            row, col, curr_effort = curr

            if row == rows - 1 and col == columns - 1:
                return curr_effort

            for dir_row, dir_col in directions:
                new_row, new_col = row + dir_row, col + dir_col
                if 0 <= new_row < rows and 0 <= new_col < columns:
                    new_effort = max(curr_effort, abs(heights[new_row][new_col] - heights[row][col]))
                    if new_effort < effort[new_row][new_col]:
                        effort[new_row][new_col] = new_effort
                        pq.put((new_row, new_col, new_effort))

        return -1