class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        """
        Append the value to the end of the Linked List.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse_list(self):
        """
        Reverse Linked List and return new reversed Linked List.
        """
        reversed_list = LinkedList()
        current = self.head
        while current:
            new_node = Node(current.value)
            new_node.next = reversed_list.head
            reversed_list.head = new_node
            current = current.next
        return reversed_list

    def as_list(self):
        """
        Convert Linked List to a list while preserving the order of the Linked List.
        """
        linked_list_as_list = []
        current = self.head
        while current:
            linked_list_as_list.append(current.value)
            current = current.next
        return linked_list_as_list

def reversed_list(values):
    initial_list = LinkedList()
    for value in values:
        initial_list.insert(value)
    reversed_list = initial_list.reverse_list()
    return reversed_list.as_list()

# Example usage
values = [1, 2, 3, 4, 5]
result = reversed_list(values)
print(result)  # Output: [5, 4, 3, 2, 1]
