class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        
        res = [root.val]

        def dfs(root):
            if not root:
                return 0
            
            leftSum = dfs(root.left)
            rightSum = dfs(root.right)

            splitSum = leftSum + rightSum + root.val

            notSplitSum = max(leftSum, rightSum, 0) + root.val

            res[0] = max(res[0], splitSum, notSplitSum)

            return notSplitSum

        dfs(root)

        return res[0]