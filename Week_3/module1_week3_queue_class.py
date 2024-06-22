"""Question 4 of homework Module 1 Week 3."""


class MyQueue():
    """Create a class to display how Queue works in Python."""

    def __init__(self, capacity):
        """Initialize the queue by getting max value and an empty list."""
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        """Check if the queue is empty."""
        if len(self.__queue) == 0:
            return True
        else:
            return False

    def is_full(self):
        """Check if the queue is full."""
        if len(self.__queue) == self.__capacity:
            return True
        else:
            return False

    def dequeue(self):
        """Remove the first element from the queue."""
        if self.is_empty():
            return None
        else:
            return self.__queue.pop(0)

    def enqueue(self, value):
        """Add an element to the queue."""
        if self.is_full():
            return None
        else:
            self.__queue.append(value)

    def front(self):
        """Return the first element in the queue."""
        if self.is_empty():
            return None
        else:
            return self.__queue[0]


# Test cases
if __name__ == "__main__":
    queue = MyQueue(5)
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.is_full())
    print(queue.front())
    print(queue.dequeue())
    print(queue.front())
    print(queue.dequeue())
    print(queue.is_empty())
