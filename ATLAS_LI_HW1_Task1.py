"""
Problem 1: An array of elements is given.
The task is to find the next greater for each element in the array.

If there is no greater element to the right of the element, then return -1.

While a brute-force solution using nested loops has a time complexity of (n^2),

the required solution shouldhave a time complexity of O(n), which can be
achieved using a stack

Sample Input: [2, 1, 4, 3]
Sample Output: [4, 4, -1, -1]
"""

from typing import List


def next_greater_element(x: List[int]) -> List[int]:
    """
    From right to left add itms from list x to the stack

    on every loop, pop from the stack until the top value is less than x[i] 

    after the while loop if the stack is not empty, add that value to the results list
    """

    n = len(x)
    res = [-1] * n

    # array acting as stack as we will only be changing the value at the end of the array
    stack: List[int] = []

    for i in range(n - 1, -1, -1):

        # remove values less than the current value from the stack
        while stack and stack[-1] <= x[i]:

            stack.pop()

        # adds the top value of the stack to the stack, only if there is a
        # stack because of the first iteration of the loop
        if stack:

            res[i] = stack[-1]

        # appends the current value to the stack
        stack.append(x[i])

    return res


if __name__ == "__main__":

    arr1 = [2, 1, 4, 3]

    # output [4, 4, -1, -1]
    print(next_greater_element(arr1))

    arr2 = [1, 5, 0, 2]

    # output [5, -1, 2, -1]
    print(next_greater_element(arr2))

    arr3 = [0, 0, 0, 4]

    # output [4, 4, 4, -1]
    print(next_greater_element(arr3))

    arr4 = [1, 0, 0, 0]

    # output [-1, -1, -1, -1]
    print(next_greater_element(arr4))
