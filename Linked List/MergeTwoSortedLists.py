#TC: O(n+m)
#SC: O(1)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        temp = dummy

        while list1 and list2:
            newNode = None

            if list1.val <= list2.val:
                newNode = ListNode(list1.val)
                list1 = list1.next

            else:
                newNode = ListNode(list2.val)
                list2 = list2.next

            temp.next = newNode
            temp = temp.next
        
        if not list1:
            temp.next = list2
        
        if not list2:
            temp.next = list1

        return dummy.next