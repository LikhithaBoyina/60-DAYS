class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    # Create a dummy node to act as the head of the merged list
    dummy = ListNode()
    current = dummy

    # Traverse both lists and attach the smaller node to the current
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach the remaining part of list1 or list2, whichever is non-empty
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the next node of dummy, which is the head of the merged list
    return dummy.next

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage:
list1 = createLinkedList(list(map(int,input().split())))
list2 = createLinkedList(list(map(int,input().split())))
merged = mergeTwoLists(list1, list2)
printLinkedList(merged)
