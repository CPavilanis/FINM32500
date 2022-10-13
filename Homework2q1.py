def removeNodes(listHead, x):
    # Write your code here

    dummy = SinglyLinkedListNode(0)
    dummy.next = listHead

    cur,prev = listHead,dummy

    while cur:
        if cur.data > x:
            prev.next = cur.next
        else:
            prev = cur

        cur = cur.next

    
    return dummy.next
