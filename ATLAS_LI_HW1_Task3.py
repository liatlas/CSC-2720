"""
Problem 3: Given a Circular Linked List node, which is sorted in non-descending order

write a function to insert a value insertVal into the list such that it
remains a sorted circular list.

The given node can be a reference to any single node in the list and may
not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any
place to insert the new value. After the insertion, the circular list
should remain sorted.

If the list is empty (i.e., the given node is null), you should create a
new single circular list and return the reference to that single node.
Otherwise, you should return the originally given node

Sample Input: head = [3,4,1], insertVal = 2
Sample Output: [3,4,1,2
"""

class Node:

    def __init__(self, value = None, next = None):

        self.value = value
        self.next = next

class CircularLinkedList:

    """
    what is a circular linked list?
    a list where the tail points to the head,
    however the head is not acutally needed as the head will always just be the next value of the tail
    """

    def __init__(self):

        self.tail = None

    def is_empty(self):

        return self.tail == None

    def insert(self, item):

        """
        if the cll is empty create a new cll
        if not, add a new node so that
        the list maintains non-ascending order
        """

        new_node = Node(item)

        if self.is_empty():

            """creates the new cll"""

            self.tail = new_node
            self.tail.next = new_node

    def print_list(self):

        if self.tail == self.tail.next:

            print(self.tail.value)

        else:

            head = self.tail.next

            while head.next != self.tail.next:

                print(head.value)
                head = head.next


if __name__ == "__main__":

    cll1 = CircularLinkedList()

    cll1.insert(1)

    cll1.print_list()