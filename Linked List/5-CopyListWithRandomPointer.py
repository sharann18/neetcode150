#TC: O(n)
#SC: O(n)

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2copy = {None : None}
        
        temp = head
        while temp:
            newNode = Node(x=temp.val)
            old2copy[temp] = newNode
            temp = temp.next
        
        temp = head
        while temp:
            if temp.next:
                old2copy[temp].next = old2copy[temp.next]
            if temp.random:
                old2copy[temp].random = old2copy[temp.random]

            temp = temp.next

        return old2copy[head]