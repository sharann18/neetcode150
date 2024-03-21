#TC: O(n*m)
#SC: #SC: O(n) for unbalanced tree; O(logn) for balanced tree
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        
        return (p.val == q.val and self.isSameTree(p.left, q.left) and 
        self.isSameTree(p.right, q.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not subRoot:
            return True

        return (self.isSubtree(root.left, subRoot) or 
        self.isSubtree(root.right, subRoot) or self.isSameTree(root, subRoot))