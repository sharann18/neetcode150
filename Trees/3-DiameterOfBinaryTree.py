#TC: O(n)
#SC: O(n) for unbalanced tree; O(logn) for balanced tree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode], height=1) -> int:
        maxDia = [0]

        def dfsHeight(root):
            if not root:
                return -1
            
            leftHeight = dfsHeight(root.left)
            rightHeight = dfsHeight(root.right)

            maxDia[0] = max(maxDia[0], leftHeight + rightHeight + 2)

            return 1 + max(leftHeight, rightHeight)
        
        dfsHeight(root)
        return maxDia[0]