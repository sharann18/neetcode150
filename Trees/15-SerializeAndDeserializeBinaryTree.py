class Codec:

    def serialize(self, root):
        data = []

        def dfs(root):
            if not root:
                data.append('N')
                return
            data.append(str(root.val))

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return ','.join(data)

    def deserialize(self, data):
        nodeVals = data.split(',')
        self.i = 0

        def dfs():
            if nodeVals[self.i] == 'N':
                self.i += 1
                return None
            
            newNode = TreeNode(int(nodeVals[self.i]))
            self.i += 1
            
            newNode.left = dfs()
            newNode.right = dfs()

            return newNode
        
        return dfs()