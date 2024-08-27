"""Question 3 of homework Module 1 Week 3."""


class MyStack():
    """Create a class to display how Stack works in Python."""

    def __init__(self, capacity):
        """Define capacity attribute + create an empty list to store results."""
        self.__capacity = capacity
        self.__stack = []

    def is_full(self):
        """Write the condition when the stack is full."""
        if len(self.__stack) == self.__capacity:
            return True
        else:
            return False

    def is_empty(self):
        """Write the condition when the stack is empty."""
        if len(self.__stack) == 0:
            return True
        else:
            return False

    def pop(self):
        """Write the function to pop the top value of the stack."""
        if self.is_empty():
            print("Stack is empty, do nothing")
        else:
            self.__stack.pop(-1)

    def push(self, value):
        """
        Write the function to add values at the top of the stack.

        Input:
            value (int): The value to be added.

        Return:
            Print a string if the stack is full, or add the value to the stack.
        """
        if self.is_full():
            print("Stack is full, do nothing")
        else:
            self.__stack.append(value)

    def top(self):
        """Return the value at the top of the stack without removing it."""
        if self.is_empty():
            print("Stack is empty, no top value to return")
        else:
            return self.__stack[-1]


# Test cases
if __name__ == "__main__":
    my_stack = MyStack(5)
    my_stack.push(1)
    my_stack.push(2)
    print(my_stack.is_full())
    print(my_stack.top())
    my_stack.pop()
    print(my_stack.top())
    my_stack.pop()
    print(my_stack.is_empty())
