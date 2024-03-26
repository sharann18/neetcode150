#TC: O(n)
#SC: O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrder = []

        def dfs(root):
            if not root:
                return
    
            dfs(root.left)

            inOrder.append(root.val)
            
            dfs(root.right)
        
        dfs(root)
        
        return inOrder[k - 1]