#TC: O(max(m,n))
#SC: O(max(m,n))

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        newHead = dummy

        carry = 0

        while l1 or l2 or carry == 1:
            sum = 0

            if l1:
                sum += l1.val
            
            if l2:
                sum += l2.val
            
            sum += carry

            carry = sum // 10
            dummy.next = ListNode(val=sum%10)

            if l1: l1 = l1.next
            if l2: l2 = l2.next
            dummy = dummy.next

        return newHead.next