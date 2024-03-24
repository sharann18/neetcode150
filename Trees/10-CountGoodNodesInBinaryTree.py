#TC: O(n)
#SC: O(h)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                maxVal = max(node.val, maxVal)
                count = 1
            else:
                count = 0
            
            count += dfs(node.left, maxVal)
            count += dfs(node.right, maxVal)
            return count
        
        return dfs(root, root.val)