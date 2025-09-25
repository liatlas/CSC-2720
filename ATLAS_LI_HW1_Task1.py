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
    """
    returns an array


    """

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


if __name__ == "__main__":

    arr1 = [2, 1, 4, 3]

    print(next_greater_element(arr1))

    # output [4, 4, -1, -1]
