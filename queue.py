"""Classes for the queue"""


class Node(object):
    """Node class for linked list elements"""

    def __init__(self, data, next_node=None):
        """Create a Node"""
        self.data = data
        self.next = next_node

    def __repr__(self):
        """Representation of a node"""
        return f"<Node data={self.data}>"


class LinkedList(object):
    """Linked list class"""

    def __init__(self, head=None):
        self.head = head
        self.tail = head

    def append(self, data):
        """Add new node with given data to end of linked list"""

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node

    def remove(self, value):
        """Remove and return node with matching data from linked list"""

        prev = None

        for node in self.all():
            if node.data == value:
                if node is self.head:
                    self.head = node.next
                else:
                    prev.next = node.next
                if node is self.tail:
                    self.tail = prev
                return node
            prev = node

        return None

    def find(self, value):
        """Return whether node with matching data is in linked list"""

        for node in self.all():
            if node.data == value:
                return True

        return False

    def all(self):
        """Generator object that yields next item in the linked list"""

        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __repr__(self):
        """Representation of the queue"""

        if self.head:
            return f"<Linked List: head={self.head.data} tail={self.tail.data}>"
        else:
            return f"<Linked List: head={self.head} tail={self.tail}>"


class Queue(object):
    """Hackbright Queue class"""

    def __init__(self):
        self._list = LinkedList()

    def push(self, value):
        """Add an element to the end of the linked list"""

        self._list.append(value)

    def pop(self):
        """Remove the first element from the linked list"""

        if self.is_empty():
            return None
        else:
            return self._list.remove(self._list.head.data)

    def peek(self):
        """Return first user in queue without modifying linked list"""

        if self.is_empty():
            return None
        else:
            return self._list.head.data

    def is_empty(self):
        """Return boolean for whether the queue is empty"""

        return self._list.head is None

    def empty(self):
        """Empty the queue"""
        self._list = LinkedList()

    def __repr__(self):
        """Representation of the queue"""
        return "<HB Queue>"

    def __str__(self):
        """String format for the queue"""

        q_str = "[ "

        # Add each node's data to the string
        for node in self._list.all():
            q_str += node.data + " "

        # Add a random emoji for empty queues
        if self.is_empty():
            q_str += ":emoji: "

        q_str += "]"

        return q_str
