from collections import deque
from typing import Optional, List


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
