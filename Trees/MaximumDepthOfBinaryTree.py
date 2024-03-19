#TC: O(n)
#SC: O(n) for skewed tree; O(logn) for balanced tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode], height=1) -> int:
        if not root:
            return height - 1
            
        heightLeft = self.maxDepth(root.left, height+1)
        heightRight = self.maxDepth(root.right, height+1)

        return max(heightLeft, heightRight)