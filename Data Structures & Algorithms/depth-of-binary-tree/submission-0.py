# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
    # Intuition
        # Recursive DFS computes the maximum depth of a binary tree by exploring every node.
        # If a node is None, its depth is 0.
    # Algorithm
        # if root is null, we return 0
        # Otherwise, we recursively compute the leftDepth and the rightDepth.
        # Return the max of either the leftDepth or the rightDepth + 1 for the current node
    # Time and Space Complexity
        # Time - O(n)
        # Space - O(h)
        
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))