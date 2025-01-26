'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # Step 1: Detect the loop using Floyd's Cycle Detection
        slow = head
        fast = head
        loop_exists = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                loop_exists = True
                break
        
        # If no loop exists, return True
        if not loop_exists:
            return True
        
        # Step 2: Find the start of the loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Step 3: Remove the loop
        start_of_loop = slow
        ptr = start_of_loop
        while ptr.next != start_of_loop:
            ptr = ptr.next
        
        ptr.next = None  # Break the loop
        
        return True
    
    # Utility function to create a linked list with a loop
    def createLinkedList(arr, pos):
        if not arr:
            return None
        head = Node(arr[0])
        temp = head
        loop_node = None
        
        for i in range(1, len(arr)):
            temp.next = Node(arr[i])
            temp = temp.next
            if i == pos - 1:
                loop_node = temp
        
        if pos != 0:
            temp.next = loop_node
        
        return head
    



#{ 
 # Driver Code Starts
# driver code:


class Node:

    def __init__(self, val):
        self.next = None
        self.data = val


class linkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, num):
        if self.head is None:
            self.head = Node(num)
            self.tail = self.head
        else:
            self.tail.next = Node(num)
            self.tail = self.tail.next

    def isLoop(self):
        if self.head is None:
            return False

        fast = self.head.next
        slow = self.head

        while slow != fast:
            if fast is None or fast.next is None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def loopHere(self, position):
        if position == 0:
            return

        walk = self.head
        for _ in range(1, position):
            walk = walk.next
        self.tail.next = walk

    def length(self):
        walk = self.head
        ret = 0
        while walk:
            ret += 1
            walk = walk.next
        return ret


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        arr = tuple(int(x) for x in input().split())
        pos = int(input())
        n = len(arr)
        ll = linkedList()
        for i in arr:
            ll.add(i)
        ll.loopHere(pos)

        Solution().removeLoop(ll.head)

        if ll.isLoop() or ll.length() != n:
            print("false")
            continue
        else:
            print("true")
        print("~")

# } Driver Code Ends