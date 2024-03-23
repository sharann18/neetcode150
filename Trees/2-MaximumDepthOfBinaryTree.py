#TC: O(n)
#SC: O(n) for skewed tree; O(logn) for balanced tree
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=1) -> int:
        if not root:
            return depth - 1
            
        depthLeft = self.maxDepth(root.left, depth+1)
        depthRight = self.maxDepth(root.right, depth+1)

        return max(depthLeft, depthRight)