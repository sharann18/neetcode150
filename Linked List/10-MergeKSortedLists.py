#Using minHeap
#TC: O(nlog(n)); because inserting an element into the heap is an O(logn) operation.
#SC: O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapify(heap)
        dummy = ListNode()
        newList = dummy

        for l in lists:
            while l:
                heappush(heap, l.val)
                l = l.next
        
        while heap:
            nodeVal = heappop(heap)
            newNode = ListNode(val=nodeVal)
            dummy.next = newNode
            dummy = dummy.next

        return newList.next

#Recursive solution
#TC: O(nlog(k))
#SC: O(n)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedList = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedList.append(self.merge2Lists(list1, list2))
            lists = mergedList

        return lists[0]
    
    def merge2Lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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