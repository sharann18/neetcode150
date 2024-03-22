#TC: O(n)
#SC: O(n)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = deque()

        queue.append(root)

        while queue:
            
            subRes = []

            for i in range(0, len(queue)):
                currNode = queue.popleft()
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
                
                subRes.append(currNode.val)
            
            res.append(subRes)
        
        return res