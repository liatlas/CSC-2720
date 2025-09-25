"""
Problem 2: Standard web browsers contain features to move backward and forward among the pages recently visited. One way to implement these features is to use two stacks to keep track of the pages that can be reached by moving backward and forward.

You are asked to simulate this feature as a Python console application. The application should accept the following commands:

1. BACK: If the backward stack is empty, the command is ignored. Otherwise, push the current page on the top of the forward stack. Pop the page from the top of the backward stack, making it the new current page.

2. FORWARD: If the forward stack is empty, the command is ignored. Otherwise, push the current page on the top of the backward stack. Pop the page from the top of the forward stack, making it the new current page.

3. VISIT <url>: Push the current page on the top of the backward stack, and make the URL specify the new current page. The forward stack is emptied.

4. QUIT: Quit the application. Consider handling any exceptional scenarios (e.g. invalid attempts to go BACK or FORWARD, missing ‘url’ for the visit command, misspelled/invalid commands etc.).

Input
Input contains a series of commands. The keywords BACK, FORWARD, VISIT, and QUIT are all in uppercase. URLs have no whitespace and have at most 50 characters. The end of input is indicated by the QUIT command and the application should terminate when this command is received.

Output For each command, print the URL of the current page (in a line) after the command is executed if the command is not ignored. Otherwise, print Ignored
"""
