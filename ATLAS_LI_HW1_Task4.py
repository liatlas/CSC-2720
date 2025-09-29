"""
Round Robin Scheduler

if the process is completed, print it and remove it from the list

if not move on

input:

a list of process ids the process id and its burst time

the time quantum (how much time each process gets to run before moving on)

output:

the remaining burst time for the process

total time taken

each process gets the same amount of time
after that cycle update burst time for that node
if that time is zero then
"""


class Node:
    """
    Node Class

    stores:

        pid
        burst_time (time each process needs/ also will serve as time left)
        next_process (next)
    """

    _next_pid: int = 1

    def __init__(self, burst_time: int = None):

        self.pid = Node._next_pid
        Node._next_pid += 1

        self.burst_time = burst_time
        self.next = None


class CircularLinkedList:
    """
    CircularLinkedList Class

    append(pid, burst_time): Add a new process to the circular
    linked list.

    remove(node): Remove a process from the list. (once the process is done / burst_time is 0)

    display(): Display all processes and their remaining burst time.

    is_empty(): Check if all processes are completed (i.e., list is empty).
    """

    def __init__(self):

        self.tail = None

    def append(self, time):
        """
        creates a new node with burst_time = time

        if the ll is empty link it to itself

        if not slot the new_node in at the tail of the ll
        """

        new_node = Node(time)

        if self.is_empty():

            self.tail = new_node
            self.tail.next = new_node

            return

        new_node.next = self.tail.next
        self.tail.next = new_node
        self.tail = new_node

        return new_node

    def remove(self, node):
        """
        removes the inputed node from the list
        """

        if self.is_empty():  # empty list

            return

        if self.tail is node and self.tail.next is node:  # list has one node

            self.tail = None
            return

        prev = self.tail
        cur = self.tail.next

        while True:

            if cur is node:

                break

            prev = cur
            cur = cur.next

        prev.next = cur.next

        if node is self.tail:

            self.tail = prev

    def display(self):
        """
        display processes in format
        Processes in the list:
        Process 1: Remaining Burst Time = <burst_time>
        Process 2: Remaining Burst Time = <burst_time>
        ...

        """
        if self.is_empty():

            print("All processes completed")
            return

        print("Processes in the list:")

        cur = self.tail.next

        while True:

            print(
                f"Process {cur.pid}: Remaining Burst Time = {cur.burst_time}")

            if cur is self.tail:

                break

            cur = cur.next

    def is_empty(self):
        """
        return true if empty
        """

        return self.tail is None

    def round_robin(self, quantum: int):

        print("Starting Round Robin Scheduling:")

        total_time = 0

        current = self.tail.next

        while not self.is_empty():

            run_time = quantum if current.burst_time > quantum else current.burst_time

            current.burst_time -= run_time

            print(f"Time: {total_time}, Processing PID: {current.pid}")
            print(
                f"Process {current.pid} now has {current.burst_time} units remaining.")

            total_time += run_time

            next_node = current.next

            if current.burst_time <= 0:

                print(f"Process {current.pid} completed.")

                self.remove(current)

                if self.is_empty():

                    break

                current = next_node

            else:

                self.tail = current
                current = next_node


def main():

    cll = CircularLinkedList()

    cll.append(4)
    cll.append(10)
    cll.append(1)

    cll.display()

    cll.round_robin(4)


if __name__ == "__main__":

    main()
