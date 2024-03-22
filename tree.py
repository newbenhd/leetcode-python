from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = ""


class Trie:
    def __init__(self):
        self.node = Node()

    def insert(self, word: str) -> None:
        node = self.node
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end = True
        node.word = word

    def search(self, word: str) -> bool:
        node = self.node
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


class WordDictionary:
    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        tree = self.tree
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree["*"] = {}

    def search(self, word: str) -> bool:
        def dfs(i: int, counter: int, tree: dict) -> bool:
            if counter > 2:
                return False
            if i == len(word):
                return "*" in tree
            if word[i] == ".":
                for child in tree.values():
                    if dfs(i + 1, counter + 1, child):
                        return True
                return False
            return dfs(i + 1, counter, tree[word[i]]) if word[i] in tree else False

        return dfs(0, 0, self.tree)


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # preorder dfs to check left, top, right, bottom sequentially. Mark visited cell.
        # skip cell which is marked and out of bound. backtrace the cell when child finished searching.
        # continue until all board cell was visited or word was found.
        # save the found word to output
        # refresh board when dfs finished and continue with next word.
        output = set()

        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(node: Node, r, c):
            if node.end:
                output.add(node.word)
            if (
                not node.children
                or r < 0
                or r >= len(board)
                or c < 0
                or c >= len(board[0])
                or board[r][c] == "*"
            ):
                return
            cell = board[r][c]
            board[r][c] = "*"
            if cell in node.children:
                dfs(node.children[cell], r + 1, c)
                dfs(node.children[cell], r - 1, c)
                dfs(node.children[cell], r, c + 1)
                dfs(node.children[cell], r, c - 1)
            board[r][c] = cell

        for r in range(len(board)):
            for c in range(len(board[r])):
                cell = board[r][c]
                board[r][c] = "*"
                if cell in trie.node.children:
                    node = trie.node.children[cell]
                    dfs(node, r + 1, c)
                    dfs(node, r - 1, c)
                    dfs(node, r, c + 1)
                    dfs(node, r, c - 1)
                board[r][c] = cell
        return list(output)

    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        # postorder dfs to check if left child is p or q. check if current node is p or q. if either p or q was found, then another one
        # might be on right subtree. This assumption applies on any size of tree.
        # if another one was on right subtree, the LCA should be the current node, else, go parent node and do the procesure again.
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder dfs traversal and count the number of traverse. if the track number is equal to k,
        # then return the node value.
        # Recursion:
        # Base case: root is None or k == track count
        # Inorder dfs
        output, count = -1, 0

        def inorder(node: Optional[TreeNode]):
            nonlocal output, count
            if not node or count > k:
                return
            inorder(node.left)
            count += 1
            if count == k:
                output = node.val
                return
            inorder(node.right)

        inorder(root)
        return output

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal. And compare node.val and previous value (the starting previous value is negative infinity).
        # if the comparison returns node.val is lower than prev value, then return False
        # otherwise, reassign previous value to node.val. And go next.
        lowest = -float("inf")

        def inorder(node: Optional[TreeNode]) -> bool:
            nonlocal lowest
            if not node:
                return True
            if not (inorder(node.left) and lowest < node.val):
                return False
            lowest = node.val
            return inorder(node.right)

        return inorder(root)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # post-dfs carrying level depth from child to parent
        # Recursion
        # base case: root == null; then return 0
        # each stack carrys previous level + 1
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # preorder dfs to check current node of tree 1 is equal to current node of tree 2
        # Recursion
        # base case:
        #   p != q -> return false
        #   both p and q is None -> return true
        # P(n):
        #   P(n-1) and p == q
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # preorder dfs to swap current node left and right child. Continue until no child
        # Base: left and right are None
        # Base: current node is None
        # F(n): swap(l, r) + F(n-1)
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # post-order dfs
        # current node should check path for both child.
        # any node that has both child positive, then path is established.
        # otherwise, return one or none of the child which is positive.
        # also, remember if adding child to current node returns negative,
        # it's better not to include it into path. In the case, path is
        # already established on either left, right, or current node based on
        # the highest value of them.
        # Recursion:
        # Base case: if current node is empty. return zero.
        if not root:
            return 0
        output = root.val

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal output
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            output = max(output, left + right + node.val)
            highest = max(left + node.val, right + node.val, node.val, 0)
            return highest

        dfs(root)
        return output

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use bfs to traverse the tree by level. Also, keep track of each
        # level. And push the node on each level to list dedicated to the level.
        # Use queue
        output = []

        def bfs(node, level):
            if not node:
                return
            if level == len(output):
                output.append([])
            output[level].append(node.val)
            bfs(node.left, level + 1)
            bfs(node.right, level + 1)

        bfs(root, 0)
        return output

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # inorder dfs traversal from root. If current node matches to subRoot, then start the validation.
        # if none of subRoot matches from dfs validation, then return false. If all the nodes of subRoot matches
        # on dfs traversal node, then return true
        # Recursion:
        # Base: when current node is None, then return

        if not root:
            return False
        if not subRoot:
            return True
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        mid = inorder.index(preorder[0])
        return TreeNode(
            preorder[0],
            self.buildTree(preorder[1 : mid + 1], inorder[:mid]),
            self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :]),
        )


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # postorder dfs with node value separate by comma, with empty
        # child as empty string
        if not root:
            return "#"
        return (
            str(root.val)
            + ","
            + self.serialize(root.left)
            + ","
            + self.serialize(root.right)
        )

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(q: deque):
            val = q.popleft()
            if val == "#":
                return None
            parent = TreeNode(int(val))
            parent.left = dfs(q)
            parent.right = dfs(q)
            return parent

        return dfs(deque(data.split(",")))


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
