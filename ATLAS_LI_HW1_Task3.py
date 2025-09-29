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

    def __init__(self, value: int = None, next = None):

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
        self.size = 0

    def is_empty(self):
        """if the cll is empty return True"""

        return self.size == 0

    def __len__(self):

        return self.size

    def insert(self, item: int):
        """
        This will be used to add values to the list as well as the order in which they are added is always non-ascending

        if the list is not empty
        there will be a series of checks performed while iterating through the list

        check one: the item first between the current and the next
        check two: at the point where the loop wraps, does the item fit there?
        check three: have we reached the end
        """

        new_node = Node(item)

        if self.is_empty():

            self.tail = new_node
            self.tail.next = new_node

            self.size = 1

            return

        current = self.tail

        while True:

            if current.value <= item <= current.next.value:  # check 1

                break

            if current.value > current.next.value:  # check 2

                if item >= current.value or item <= current.next.value:

                    break

            current = current.next

            if current == self.tail:  # check 3

                break

        new_node.next = current.next
        current.next = new_node

        # When inserted at the end of the list, the tail of the list does not move and should be shift over
        if current == self.tail:

            self.tail = new_node

        self.size += 1

    def print_list(self):

        if self.tail == self.tail.next:

            print(self.tail.value)

        else:

            current = self.tail.next

            for i in range(self.size):

                print(current.value)

                current = current.next


if __name__ == "__main__":

    cll1 = CircularLinkedList()

    cll1.insert(3)
    cll1.insert(4)
    cll1.insert(1)

    cll1.insert(2)

    print("print len")
    print(len(cll1))

    print("print list")
    cll1.print_list()

    cll2 = CircularLinkedList()

    cll2.insert(50)
    cll2.insert(30)

    cll2.insert(40)
    cll2.insert(80)

    print("print list")
    cll2.print_list()
