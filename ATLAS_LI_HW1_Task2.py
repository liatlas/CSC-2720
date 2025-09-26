"""
Problem 2: Standard web browsers contain features to move backward and forward among the pages recently visited. One way to implement these features is to use two stacks to keep track of the pages that can be reached by moving backward and forward.

You are asked to simulate this feature as a Python console application. The application should accept the following commands:

1. BACK: If the backward stack is empty, the command is ignored. Otherwise, push the current page on the top of the forward stack. Pop the page from the top of the backward stack, making it the new current page.

2. FORWARD: If the forward stack is empty, the command is ignored. Otherwise, push the current page on the top of the backward stack. Pop the page from the top of the forward stack, making it the new current page.

3. VISIT <url>: Push the current page on the top of the backward stack, and make the URL specify the new current page. The forward stack is emptied.

4. QUIT: Quit the application. 

Consider handling any exceptional scenarios (e.g. invalid attempts to go BACK or FORWARD, missing ‘url’ for the visit command, misspelled/invalid commands etc.).

Input
Input contains a series of commands. The keywords BACK, FORWARD, VISIT, and QUIT are all in uppercase. URLs have no whitespace and have at most 50 characters. The end of input is indicated by the QUIT command and the application should terminate when this command is received.

Output For each command, print the URL of the current page (in a line) after the command is executed if the command is not ignored. Otherwise, print Ignored
"""
import sys
from typing import Optional, List

class TwoStack:

    def __init__(self):

        self._fstack: List[str] = []
        self._bstack: List[str] = []
        self._current = None
    
    def back(self) -> Optional[str]:

        if self._bstack != []:

            self._fstack.append(self._current)
            self._current  = self._bstack.pop()

            print(self._current)

        else:

            print("Ignored")

    def forward(self) -> Optional[str]:

        if self._fstack != []:

            self._bstack.append(self._current)
            self._current = self._fstack.pop()

            print(self._current)
        
        else:

            print("Ignored")


    def visit(self, link: str) -> str:

        self._bstack.append(self._current)
        self._current = link

        while self._fstack:

            self._fstack.pop()

        print(self._current)

    def quit(self):
        sys.exit(0)
    

if __name__ == "__main__":

    ts1 = TwoStack()

    command_list = dict({"FOWARD": ts1.forward, "BACKWARD": ts1.back, "VISIT": ts1.visit, "QUIT": ts1.quit})

    print("--Enter the site that you want to visit--")

    while True:
        
        command = None
        arg = None

        i = input().strip().split(maxsplit = 1)

        command = str(i[0]) if i else None
        arg = i[1] if len(i) > 1 else None

        if arg and not (len(arg) < 50 and " " not in arg):

            print("--Please print a valid command - url cannot contain spaces or be greater than 50 characters--")
            continue

        if command in command_list.keys():

            func = command_list[command]

        else:

            print("--Please print a valid command--")
            continue
            
        if arg is not None:
            func(arg)
        else:
            func()
