# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, cur_sum):
            if not node:
                return 0
            
            cur_sum = cur_sum * 10 + node.val
            if not node.left and not node.right:
                return cur_sum
                
            left = dfs(node.left, cur_sum)
            right = dfs(node.right, cur_sum)
            return left + right
        
        return dfs(root, 0)
            
            
            
        