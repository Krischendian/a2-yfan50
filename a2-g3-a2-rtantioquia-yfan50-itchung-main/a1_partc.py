#    Main Author(s):  Yuhong Fan
#    Main Reviewer(s): In Tae Chung


# Stack Class Implementation
class Stack:
    """
    A stack implementation using a Python list with a fixed capacity. It follows the Last In, First Out (LIFO) principle.
    Prohibited operations: append(), pop(), insert().
    """

    def __init__(self, cap = 10): # Add a default capacity
        """
        Initializes a new stack with a specified capacity.
        
        :param cap: Integer representing the stack's capacity.
        """
        self.items = [None] * cap  # Underlying storage for stack items
        self.n = 0  # Number of items currently in the stack
        self.cap = cap  # Total capacity of the stack

    def capacity(self):
        """
        Returns the current capacity of the stack.
        
        :return: Integer representing the stack's capacity.
        """
        return self.cap

    def push(self, data):
        """
        Adds an item to the top of the stack. May trigger a resize operation if the stack is full.
        
        :param data: The item to be added to the stack.
        """
        if self.n == self.cap:
            self.resize(2 * self.cap)  # Double the capacity upon reaching the limit
        self.items[self.n] = data
        self.n += 1

    def pop(self):
        """
        Removes and returns the item from the top of the stack.
        
        :return: The item at the top of the stack.
        :raises IndexError: If the stack is empty.
        """
        if self.n == 0:
            raise IndexError('pop() used on empty stack')
        self.n -= 1
        return self.items[self.n]

    def get_top(self):
        """
        Returns the item at the top of the stack without removing it.
        
        :return: The top item of the stack, or None if the stack is empty.
        """
        return None if self.n == 0 else self.items[self.n - 1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        
        :return: True if the stack is empty, False otherwise.
        """
        return self.n == 0

    def __len__(self):
        """
        Returns the number of items in the stack.
        
        :return: The number of items as an integer.
        """
        return self.n

    def resize(self, new_cap):
        """
        Resizes the stack's capacity.
        
        :param new_cap: The new capacity as an integer.
        """
        new_storage = [None] * new_cap
        for i in range(self.n):
            new_storage[i] = self.items[i]
        self.items = new_storage
        self.cap = new_cap

# Queue Class Implementation
class Queue:
    """
    A queue implementation using a Python list with a fixed capacity. It follows the First In, First Out (FIFO) principle.
    Prohibited operations: append(), pop(), insert().
    """

    def __init__(self, cap = 10): # Add a default capacity
        """
        Initializes a new queue with a specified capacity.
        
        :param cap: Integer representing the queue's capacity.
        """
        self.items = [None] * cap  # Underlying storage for queue items
        self.n = 0  # Number of items currently in the queue
        self.front = 0  # Index of the front item
        self.cap = cap  # Total capacity of the queue

    def capacity(self):
        """
        Returns the current capacity of the queue.
        
        :return: Integer representing the queue's capacity.
        """
        return self.cap

    def enqueue(self, data):
        """
        Adds an item to the back of the queue. May trigger a resize operation if the queue is full.
        
        :param data: The item to be added to the queue.
        """
        if self.n == self.cap:
            self.resize(2 * self.cap)  # Double the capacity upon reaching the limit
        back = (self.front + self.n) % self.cap  # Calculate the index for the new item
        self.items[back] = data
        self.n += 1

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue.
        
        :return: The item at the front of the queue.
        :raises IndexError: If the queue is empty.
        """
        if self.n == 0:
            raise IndexError('dequeue() used on empty queue')
        item = self.items[self.front]
        self.front = (self.front + 1) % self.cap  # Move front pointer forward
        self.n -= 1
        return item

    def get_front(self):
        """
        Returns the item at the front of the queue without removing it.
        
        :return: The front item of the queue, or None if the queue is empty.
        """
        return None if self.n == 0 else self.items[self.front]

    def is_empty(self):
        """
        Checks if the queue is empty.
        
        :return: True if the queue is empty, False otherwise.
        """
        return self.n == 0

    def __len__(self):
        """
        Returns the number of items in the queue.
        
        :return: The number of items as an integer.
        """
        return self.n

    def resize(self, new_cap):
        """
        Resizes the queue's capacity.
        
        :param new_cap: The new capacity as an integer.
        """
        new_storage = [None] * new_cap
        for i in range(self.n):
            new_storage[i] = self.items[(self.front + i) % self.cap]  # Realign items starting at index 0
        self.items = new_storage
        self.front = 0
        self.cap = new_cap

# Deque Class Implementation
class Deque:
    """
    A deque (double-ended queue) implementation using a Python list with a fixed capacity. Allows insertion and removal from both ends.
    Prohibited operations: append(), pop(), insert().
    """

    def __init__(self, cap = 10): # Add a default capacity
        """
        Initializes a new deque with a specified capacity.
        
        :param cap: Integer representing the deque's capacity.
        """
        self.items = [None] * cap  # Underlying storage for deque items
        self.n = 0  # Number of items currently in the deque
        self.front = 0  # Index of the front item
        self.cap = cap  # Total capacity of the deque

    def capacity(self):
        """
        Returns the current capacity of the deque.
        
        :return: Integer representing the deque's capacity.
        """
        return self.cap

    def push_front(self, data):
        """
        Adds an item to the front of the deque. May trigger a resize operation if the deque is full.
        
        :param data: The item to be added to the front of the deque.
        """
        if self.n == self.cap:
            self.resize(2 * self.cap)  # Double the capacity upon reaching the limit
        self.front = (self.front - 1 + self.cap) % self.cap  # Decrement front index circularly
        self.items[self.front] = data
        self.n += 1

    def push_back(self, data):
        """
        Adds an item to the back of the deque. May trigger a resize operation if the deque is full.
        
        :param data: The item to be added to the back of the deque.
        """
        if self.n == self.cap:
            self.resize(2 * self.cap)  # Double the capacity upon reaching the limit
        back = (self.front + self.n) % self.cap  # Calculate the index for the new item
        self.items[back] = data
        self.n += 1

    def pop_front(self):
        """
        Removes and returns the item from the front of the deque.
        
        :return: The item at the front of the deque.
        :raises IndexError: If the deque is empty.
        """
        if self.n == 0:
            raise IndexError('pop_front() used on empty deque')
        item = self.items[self.front]
        self.front = (self.front + 1) % self.cap  # Move front pointer forward
        self.n -= 1
        return item

    def pop_back(self):
        """
        Removes and returns the item from the back of the deque.
        
        :return: The item at the back of the deque.
        :raises IndexError: If the deque is empty.
        """
        if self.n == 0:
            raise IndexError('pop_back() used on empty deque')
        back = (self.front + self.n - 1) % self.cap  # Calculate the index for the last item
        item = self.items[back]
        self.n -= 1
        return item

    def get_front(self):
        """
        Returns the item at the front of the deque without removing it.
        
        :return: The front item of the deque, or None if the deque is empty.
        """
        return None if self.n == 0 else self.items[self.front]

    def get_back(self):
        """
        Returns the item at the back of the deque without removing it.
        
        :return: The back item of the deque, or None if the deque is empty.
        """
        return None if self.n == 0 else self.items[(self.front + self.n - 1) % self.cap]

    def is_empty(self):
        """
        Checks if the deque is empty.
        
        :return: True if the deque is empty, False otherwise.
        """
        return self.n == 0

    def __len__(self):
        """
        Returns the number of items in the deque.
        
        :return: The number of items as an integer.
        """
        return self.n

    def __getitem__(self, k):
        """
        Returns the k'th item from the front of the deque, without removing it.
        
        :param k: The index of the item to retrieve, where 0 is the front.
        :return: The k'th item from the front of the deque.
        :raises IndexError: If the index is out of range.
        """
        if k < 0 or k >= self.n:
            raise IndexError('Index out of range')
        index = (self.front + k) % self.cap
        return self.items[index]

    def resize(self, new_cap):
        """
        Resizes the deque's capacity.
        
        :param new_cap: The new capacity as an integer.
        """
        new_storage = [None] * new_cap
        for i in range(self.n):
            new_storage[i] = self.items[(self.front + i) % self.cap]  # Realign items starting at index 0
        self.items = new_storage
        self.front = 0
        self.cap = new_cap
