from Node import Node

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.

        The head of the linked list is initially set to None.
        """
        self.head = None

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.

        If the linked list is empty, the new node becomes the head.
        If the linked list is not empty, traverse to the end and append the new node.

        Parameters:
        value (any): The value to be stored in the new node.
        """
        node = Node(value)  # Create a new node with the given value

        # If the LinkedList is empty
        if self.head is None:
            self.head = node
        else:
            # LinkedList is not empty
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def __getitem__(self, index):
        """
        Get the value at the specified index in the linked list.

        Parameters:
        index (int): The index of the value to retrieve.

        Returns:
        any: The value stored at the specified index in the linked list.

        Raises:
        IndexError: If the index is out of range.
        """
        current = self.head
        current_index = 0
        while current:
            if current_index == index:
                return current.value
            current = current.next
            current_index += 1
        raise IndexError("Index out of range")

    
    def __str__(self):
        """
        Get a string representation of the linked list.

        Returns:
        str: A string representation of the linked list, showing node values separated by '-->'.
        """
        result = ""
        current = self.head
        while current:
            result += str(current.val) + "-->"
            current = current.next
        return result

    def __len__(self):
        """
        Get the number of nodes in the linked list.

        Returns:
        int: The number of nodes in the linked list.
        """
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length