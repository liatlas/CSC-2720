"""
Problem 4: You are given a list of processes where each process has a
Process ID (PID) and a
Burst Time (the amount of time the process requires on the CPU). The CPU uses a Round Robin
Scheduling algorithm with a fixed time quantum. Your task is to implement this scheduling using
a circular linked list where each process is represented as a node in the list.
Requirements:
1. Circular Linked List Implementation:
○ Implement a circular linked list to manage the processes.
○ Each node should represent a process and contain:
■ PID: Process ID
■ Burst Time: The time the process requires on the CPU
■ Pointer to the next process in the list
2. Round Robin Scheduling Algorithm:
○ Each process is allowed to run for the duration of the time quantum.
○ If a process finishes (its burst time becomes zero or less), it is removed from the
list.
○ If a process does not finish in the given time quantum, subtract the quantum from
its burst time and move to the next process in the list.
○ Continue the process until all processes have been completed.
3. Input/Output:
○ Input:
■ A list of processes where each process is defined by its Process ID and
Burst Time.
■ A Time Quantum defines how long each process gets to execute in each
cycle.
○ Output:
■ Print the remaining burst time of each process after each time quantum.
■ Print the total time taken for all processes to complete

Functionality:
Implement the following functionality:
1. Node Class:
○ This class should represent a process in the system and store the Process ID,
remaining burst time, and a reference to the next process.
2. CircularLinkedList Class:
○ Functions:
■ append(pid, burst_time): Add a new process to the circular
linked list.
■ remove(node): Remove a process from the list.
■ display(): Display all processes and their remaining burst time.
■ is_empty(): Check if all processes are completed (i.e., list is empty).
3. Round Robin Scheduler Function:
○ Simulate the Round Robin Scheduling by running each process for a maximum of
the given time quantum.
○ After each cycle, update the burst time of the process, and if the burst time is zero,
remove the process from the list.
○ Continue until all processes are completed, and print the total elapsed time.
Constraints:
● The number of processes can range from 1 to 50.
● The burst time of any process will be between 1 and 100 units.
● The time quantum will be between 1 and 10 units
Example:
Input:
processes = [(1, 10), (2, 5), (3, 8)] # Process ID, Burst Time
quantum_time = 4
Expected Output:
Processes in the list:
Process 1: Remaining Burst Time = 10
Process 2: Remaining Burst Time = 5
Process 3: Remaining Burst Time = 8
Due Date: Mon, Sep 29, 2025, 11:59 PM
Starting Round Robin Scheduling:
Time: 0, Processing PID: 1
Process 1 now has 6 units remaining.
Time: 4, Processing PID: 2
Process 2 now has 1 unit remaining
Time: 8, Processing PID: 3
Process 3 now has 4 units remaining.
Time: 12, Processing PID: 1
Process 1 now has 2 units remaining.
Time: 16, Processing PID: 2
Process 2 completed
Time: 17, Processing PID: 3
Process 3 completed.
Time: 21, Processing PID: 1
Process 1 completed.
All processes completed
"""
