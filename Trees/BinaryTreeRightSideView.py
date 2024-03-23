#TC: O(n)
#SC: O(n)

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res =[]

        if not root:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            currLen = len(queue)

            for i in range(0, len(queue)):
                currNode = queue.popleft()

                if currNode.left:
                    queue.append(currNode.left)
                
                if currNode.right:
                    queue.append(currNode.right)
                
                if i == currLen - 1:
                    res.append(currNode.val)
        
        return res