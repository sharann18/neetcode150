#TC: O(n)
#SC: O(n)

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def buildTreeHelper(preorder, inorder):
            if not preorder:
                return None
            
            newRoot = TreeNode(val=preorder[0])

            i = 0

            while inorder[i] != preorder[0]:
                i += 1
            
            newRoot.left = buildTreeHelper(preorder[1:i+1], inorder[0:i])
            newRoot.right = buildTreeHelper(preorder[i+1:], inorder[i+1:])

            return newRoot
        
        return buildTreeHelper(preorder, inorder)