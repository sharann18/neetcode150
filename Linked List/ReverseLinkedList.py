#TC: O(n)
#SC: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        temp = head
        tempAfter = head.next
        tempBefore = None

        while temp:
            temp.next = tempBefore
            tempBefore = temp
            temp = tempAfter
            if tempAfter: tempAfter = tempAfter.next
        
        head = tempBefore

        return head