class Node:
    def __init__(self, data):
        """Initialize a node with data and a pointer to the next node."""
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """Initialize the linked list with a head pointer."""
        self.head = None

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def traverse(self):
        """Print each element in the list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, value):
        """Find a node with a specific value."""
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def remove(self, value):
        """Remove a node from the list by value."""
        current = self.head
        previous = None
        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True  # Node removed
            previous = current
            current = current.next
        return False  # Node not found

# Example usage
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_beginning(5)
    linked_list.traverse()  # Output: 5 -> 10 -> 20 -> None

    print("Searching for 10:", linked_list.search(10))  # Output: <Node with data 10>
    print("Searching for 30:", linked_list.search(30))  # Output: None

    linked_list.remove(10)
    linked_list.traverse()  # Output: 5 -> 20 -> None

