from collections import deque
from typing import Optional, List, Tuple


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def fmtList(self):
        visited = {}
        output = []

        def dfs(node: Optional[Node]):
            if not node or node.val in visited:
                return
            output.append(list(map(lambda x: x.val, node.neighbors)))
            visited[node.val] = True
            for n in node.neighbors:
                dfs(n)

        dfs(self)

        return output


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        longest = 0
        for n in setnums:
            if n - 1 not in setnums:
                length = 1
                while n + length in setnums:
                    length += 1
                longest = max(longest, length)
        return longest

    def numIslands(self, grid: List[List[str]]) -> int:
        # if current cell is land and every edge of a cell is water, it's a land.
        # if one or more edge is not water, dfs on the edge to turn the edge land into water
        # iterate on grid and increment num of islands if the current cell is land
        #   and dfs on the current cell respectively
        H, L = len(grid), len(grid[0])
        output = 0

        def dfs(r: int, c: int):
            grid[r][c] = "0"
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < H and 0 <= nc < L and grid[nr][nc] == "1":
                    dfs(nr, nc)

        for r in range(H):
            for c in range(L):
                if grid[r][c] == "1":
                    output += 1
                    dfs(r, c)
        return output

    def pacificAtlantic_v2(self, heights: List[List[int]]) -> List[List[int]]:
        H, L = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, land):
            land.add((r, c))
            for adj in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    0 <= adj[0] < H
                    and 0 <= adj[1] < L
                    and heights[adj[0]][adj[1]] >= heights[r][c]
                    and adj not in land
                ):
                    dfs(adj[0], adj[1], land)

        for r in range(H):
            dfs(r, 0, pacific)
            dfs(r, L - 1, atlantic)
        for c in range(L):
            dfs(0, c, pacific)
            dfs(H - 1, c, atlantic)

        return list(map(lambda x: [x[0], x[1]], list(pacific & atlantic)))

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # [[1,2,3],
        #  [8,9,4],
        #  [7,6,5]]
        # 1x1: top or left is pacific ocean AND right or bottom is atlantic ocean
        # 1x2: top or left is pacific ocean AND right cell is less or bottom is atlantic ocean
        #       top is pacific ocean or left is less AND right or bottom is atlantic ocean
        # 2x1: top or left is pacific ocean AND right is pacific ocean or bottom is less
        #       top is less or left is pacific ocean AND right or bottom is atlantic ocean
        # (0, 0) <- (0,1), (1,0)
        # (0,1) <- (1,1)
        # (1,0)
        # (1,1) <- (0,1)
        pacificT = {(-1, x) for x in range(len(heights[0]))}
        pacificL = {(x, -1) for x in range(len(heights))}
        atlanticR = {(x, len(heights[0])) for x in range(len(heights))}
        atlanticB = {(len(heights), x) for x in range(len(heights[0]))}
        result = dict()

        def dfs(cell: Tuple[int, int]) -> List[Tuple[bool, bool, bool, bool]]:
            if result.get(cell) is not None:
                return result[cell]
            R, C = cell
            left = (R, C - 1)
            right = (R, C + 1)
            top = (R - 1, C)
            bottom = (R + 1, C)
            result[cell] = [False, False, False, False]
            result[cell][0] = left in pacificL
            result[cell][1] = top in pacificT
            result[cell][2] = right in atlanticR
            result[cell][3] = bottom in atlanticB
            if (
                not result[cell][0]
                and heights[left[0]][left[1]] <= heights[cell[0]][cell[1]]
            ):
                previous = dfs(left)
                result[cell][0] = previous[0] or previous[1]
            if (
                not result[cell][1]
                and heights[top[0]][top[1]] <= heights[cell[0]][cell[1]]
            ):
                previous = dfs(top)
                result[cell][1] = previous[1] or previous[0]
            if (
                not result[cell][2]
                and heights[right[0]][right[1]] <= heights[cell[0]][cell[1]]
            ):
                previous = dfs(right)
                result[cell][2] = previous[2] or previous[3]
            if (
                not result[cell][3]
                and heights[bottom[0]][bottom[1]] <= heights[cell[0]][cell[1]]
            ):
                previous = dfs(bottom)
                result[cell][3] = previous[3] or previous[2]
            return result[cell]

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                dfs((r, c))
        output = []
        for k, v in result.items():
            if (v[0] or v[1]) and (v[2] or v[3]):
                output.append([k[0], k[1]])
        return output

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbors = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        visited = []
        for [a, b] in prerequisites:
            neighbors[b].append(a)
            indegree[a] += 1

        dq = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
        while dq:
            head = dq.popleft()
            visited.append(head)
            for child in neighbors[head]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    dq.append(child)
        return len(visited) == numCourses

    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        visited: dict = {None: None}

        def dfs(p: Optional[Node]) -> Optional[Node]:
            if not p or p in visited:
                return visited[p]
            visited[p] = Node(p.val)
            visited[p].neighbors = list(
                filter(lambda x: x is not None, map(lambda y: dfs(y), p.neighbors))
            )
            return visited[p]

        return dfs(node)
