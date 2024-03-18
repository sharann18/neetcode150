#TC: O(n)
#SC: O(1)

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        left = head
        right = head
        dummy = ListNode()
        newList = dummy

        while left and right:
            i = 0
            while i < k - 1 and right:
                right = right.next
                i += 1
            
            if right: 
                nextLeft = right.next
            else:
                break

            right.next = None

            revHead = self.reverseList(left)
            dummy.next = revHead
            revTail = revHead
            while revTail.next:
                revTail = revTail.next
            
            revTail.next = nextLeft

            left = nextLeft
            right = left

            dummy = revTail
        
        return newList.next

    
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