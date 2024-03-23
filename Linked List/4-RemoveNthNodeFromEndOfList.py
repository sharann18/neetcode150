#Number of nodes - n solution
#TC: O(n)
#SC: O(1)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        numNodes = 0
        temp = head

        while temp:
            numNodes += 1
            temp = temp.next
        
        numNext = numNodes - n
        
        temp = head

        if numNext == 0:
            head = head.next
        else:
            for i in range(numNext - 1):
                temp = temp.next
            
            temp.next = temp.next.next

        return head


#Dummy node + 2 pointers with offset n
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(next=head)

        left = dummy
        right = head
        
        for i in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next