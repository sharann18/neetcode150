#Solving with a stack
#TC: O(n)
#SC: O(n)
if not head.next or not head.next.next:
            return
        
slow = head
fast = head.next

while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

temp =  slow.next
slow.next = None

stack = deque()

while temp:
    stack.append(temp)
    temp = temp.next

temp = head
tempAf = head.next

while tempAf:
    temp.next = stack.pop()
    temp.next.next = tempAf
    temp = tempAf
    tempAf = tempAf.next

if temp and stack:
    temp.next = stack.pop()
    temp.next.next = None


#Solving without a stack (reverse the second half)
#TC: O(n)
#SC: O(1)
if not head.next or not head.next.next:
            return
        
slow = head
fast = head.next

while fast and fast.next:
    fast = fast.next.next
    slow = slow.next

second = slow.next
slow.next = None

prev = None
while second:
    temp = second.next
    second.next = prev
    prev = second
    second = temp

first, second = head, prev

while second:
    firstAfter, secondAfter = first.next, second.next
    first.next = second
    second.next = firstAfter

    first, second = firstAfter, secondAfter