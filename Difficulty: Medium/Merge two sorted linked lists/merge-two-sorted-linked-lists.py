#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        # Dummy node to simplify edge cases
        dummy = Node(-1)  # Use Node instead of ListNode
        current = dummy
    
        # Traverse both lists and merge
        while head1 and head2:
            if head1.data <= head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
    
        # Append the remaining elements
        if head1:
            current.next = head1
        if head2:
            current.next = head2
    
        return dummy.next
    
    # Utility function to print a linked list
    def printList(head):
        while head:
            print(head.data, end=" -> ")
            head = head.next
        print("None")
    
    # Utility function to create a linked list from a list of values
    def createLinkedList(values):
        if not values:
            return None
        head = Node(values[0])  # Use Node instead of ListNode
        current = head
        for value in values[1:]:
            current.next = Node(value)  # Use Node instead of ListNode
            current = current.next
        return head






#{ 
 # Driver Code Starts
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=' ')
        temp = temp.next
    print()
    print("~")


def insert_sorted(head, data):
    new_node = Node(data)
    if not head or head.data >= data:
        new_node.next = head
        return new_node

    current = head
    while current.next and current.next.data < data:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        input1 = list(map(int, input().split()))
        input2 = list(map(int, input().split()))

        head1 = None
        for item in input1:
            head1 = insert_sorted(head1, item)

        head2 = None
        for item in input2:
            head2 = insert_sorted(head2, item)

        obj = Solution()
        merged_head = obj.sortedMerge(head1, head2)
        print_list(merged_head)

# } Driver Code Ends