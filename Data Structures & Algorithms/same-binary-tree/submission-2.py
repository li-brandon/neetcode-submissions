# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    # Intuition
        # If the root node and the values of its children are equal then return True
        # Does this tree only have a height of one?
    # Algorithm
        # If the root node and the values of its children are equal then return True
        # Otherwise, return False
    # Time and Space Complexity
        # Time -> O(n)
        # Space -> O(n)
    
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False