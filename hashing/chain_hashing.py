from .hashmap import HashMap
from .linked_list import LinkedListNode


class ChainHashing(HashMap):
    def put(self, key, value):
        """
        Appends/Updates a value in a LinkedList node at the hash index.

        Args:
            key: The key used to hash and insert.
            value: The value inserted to the table.

        """
        node = self.H[self.h(key)]
        while node.key is not None and node.key != key:
            node = node.next

        if node.key == key:
            node.value = value
        else:
            self.count += 1
            node.key = key
            node.value = value
            node.next = LinkedListNode()
            node.next.prev = node

        self.rehashIfRequired()

    def deleteNode(self, node):
        """
        Deletes the given linked list node.

        Args:
            node (LinkedListNode): The node to be deleted.

        """
        if node.prev is None:
            if node.next is not None:
                node.value = node.next.value
                node.key = node.next.key
                node.next = node.next.next
            else:
                node.value = None
                node.key = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def getNode(self, key):
        """
        Get the linked list node for the given key.

        Args:
            key: The key used to search the node.

        Returns:
            LinkedListNode: The node for the given key.

        """
        node = self.H[self.h(key)]
        while node.key is not None and node.key != key:
            node = node.next

        return node

    def get(self, key):
        """Return the value of the node for the given key."""
        return self.getNode(key).value

    def remove(self, key):
        """Removes the node with the given key."""
        node = self.getNode(key)
        if node.key is not None:
            self.count -= 1
            self.deleteNode(node)
