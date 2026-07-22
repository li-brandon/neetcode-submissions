# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    # Intuition
        # We want to go through each node within the binary tree and check to see if each node has values matching the provided subtree
        # Make sure to return null if there's no nodes
        # I'm thinking DFS here or we can use an iterative approach with a hashmap that maps the subtree values as a tuple
    # Algorithm
        # Check for an empty tree
        # Iterate through the tree and add each node and its children to a hashmap
        # Compare the node and its children to the subtree
        # Continue iterating until every node has been visited
    # Time and Space Complexity
        # Time -> O(n)
        # Space -> O(n)

        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        return False