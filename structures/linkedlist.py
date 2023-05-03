class Node:
    def __init__(self, data: object):
        """This class is for make a 'Node' with information and reference

        Args:
            data: object = data
            next: Node = None

        Returns: None
        Raises: None

        """
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """This class is for make a 'LinkedList' with nodes

        Args:
            head: Node

        Returns: None
        Raises: None

        """
        self.head: Node = None

    def print_list(self):
        """This def is for printing the linkedlist elements
        Args:
            temporal_node (Node): a temporal node
        Returns:
            None
        Raises:
            None
        """
        temporal_node = self.head
        while temporal_node:
            print(temporal_node.data)
            temporal_node = temporal_node.next


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.head = Node(2)
    second_node = Node(5)
    third_node = Node(8)
    linked_list.head.next = second_node
    second_node.next = third_node
    linked_list.print_list()
