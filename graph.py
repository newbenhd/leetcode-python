from typing import Optional


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
