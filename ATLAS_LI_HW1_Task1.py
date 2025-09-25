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


def next_greater_element(x):

    n = len(x)
    res = [-1] * n

    # array acting as stack as we will only be changing the value at the end of the array
    stack = []

    for i in range(n - 1, -1, -1):

        # remove values less than the current value from the stack
        while stack and stack[-1] < x[i]:

            stack.pop()

        # adds the top value of the stack to the stack, only if there is a stack because of the first iteration of the loop
        if stack:

            res[i] = stack[-1]

        #appends the current value to the stack
        stack.append(x[i])

    return res


if __name__ == "__main__":

    arr1 = [2, 1, 4, 3]

    print(next_greater_element(arr1))

    # output [4, 4, -1, -1]

    """

    brute force method O(n^2):

        iterate through each element in the array
        iterate all subsequent values
        appending the greatest value to the result array

    problems:

        each value is seen multiple times
        i want to iterate through the array once
        while already knowing the future elements

    solution: iterate from right to left instead


    n = len(x)

    res = [-1] * n

    for i in range(n):

        j = i

        while j < n:

            if x[j] > x[i]:

                res[i] = x[j]
                break

            j += 1

    return res

    """

    """

    right to left method O(n):

        iterate through the array from right to left

            if its the last value of the array value

                set the index to -1

            if not

                update a max variable and max index variable each time there is a new max

            iterate through the result array and change it to match the max

        Problem:

            index is not necesarily needed

            while still O(n), the two for loops can probably be simplified

        Next I will try to implement a stack


    n = len(x)

    res = [-1] * n

    for i in range(n - 1, -1, -1):

        if i == n - 1:

            max_element = x[i]
            max_index = i

        elif x[i] > max_element:

            max_element = x[i]
            max_index = i

    for j in range(max_index):

        if j != max_index:

            res[j] = max_element

    return res

    """

    """
    stack implementation of next greatest element


    """
