#TC: O(n)
#SC: O(h)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, leftBound, rightBound):
            if not node:
                return True
            
            if not (node.val < rightBound and node.val > leftBound):
                return False
            
            return dfs(node.left, leftBound, node.val) and dfs(node.right, node.val, rightBound)
        
        return dfs(root, float(-inf), float(inf))