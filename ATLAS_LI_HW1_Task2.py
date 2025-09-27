"""
Problem 2: recently visited funcionalty using two stacks
"""
from typing import Optional, List


class TwoStack:
    """
    use two stacks to keep track of the pages that can be reached by moving backward and forward
    """

    def __init__(self):

        self._fstack: List[str] = []
        self._bstack: List[str] = []
        self._current = None

    def back(self) -> Optional[str]:
        """
        If the backward stack is empty, the command is ignored.
        Otherwise, push the current page on the top of the forward stack.
        Pop the page from the top of the backward stack, making it the new current page
        """

        if self._bstack:

            self._fstack.append(self._current)
            self._current = self._bstack.pop()

            print(self._current)

        else:

            print("Ignored")

    def forward(self) -> Optional[str]:
        """
        If the forward stack is empty, the command is ignored.
        Otherwise, push the current page on the top of the backward stack.
        Pop the page from the top of the forward stack, making it the new current page
        """

        if self._fstack:

            self._bstack.append(self._current)
            self._current = self._fstack.pop()

            print(self._current)

        else:

            print("Ignored")

    def visit(self, link: str) -> str:
        """
        Push the current page on the top of the backward stack, and
        make the URL specify the new current page. The forward stack is emptied
        """

        self._bstack.append(self._current)
        self._current = link

        while self._fstack:

            self._fstack.pop()

        print(self._current)

    def quit(self):
        """
        Quit the application
        """
        sys.exit(0)

def main():
    """
    1. cleans input and splits it for the url
    2. create command and arg
    3. checks if arg is valid, else print error and reloop
    4. checks if command is valid
    5. if arg exists use it in the function, else use the function without it
    """

    ts1 = TwoStack()

    # valid commands, since there is only one stack (eg. one browser tab)
    # the output can directly be the command of the tstack
    command_list = dict(
        {"FORWARD": ts1.forward, "BACK": ts1.back, "VISIT": ts1.visit, "QUIT": ts1.quit}
    )

    print("--Enter the site that you want to visit--")


    while True:

        command = None
        arg = None

        # strip removes leading and trailing spaces
        # split(maxsplit = 1) splits the string an array of two elements
        # (by default split by space)
        i = input().strip().split(maxsplit=1)

        # else None is not really necessary for setting command variable
        # but it will be kept nonetheless
        command = str(i[0]) if i else None
        arg = i[1] if len(i) > 1 else None

        # check that the length of arg is less than 50 and does not contain
        # whitespaces
        # as defined by the instructions
        if arg and not (len(arg) < 50 and " " not in arg):

            print(
                "--Url cannot contain spaces or be greater than 50 characters--"
            )
            continue

        # call method
        if command in command_list:

            func = command_list[command]

        else:

            print("--Please print a valid command--")
            continue

        if arg is not None:
            func(arg)
        else:
            func()



if __name__ == "__main__":
    main()
