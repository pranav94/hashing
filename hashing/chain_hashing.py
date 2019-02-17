from .hashmap import HashMap
from .linked_list import LinkedListNode


class ChainHashing(HashMap):
    def put(self, key, value):
        node = self.H[self.h(key)]
        while node.key is not None and node.key != key:
            node = node.next

        if node.key == key:
            node.value = value
        else:
            node.key = key
            node.value = value
            node.next = LinkedListNode()
            node.next.prev = node

        if self.count / self.capacity > self.load_factor:
            self.rehash()

    def deleteNode(self, node):
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
        node = self.H[self.h(key)]
        while node.key is not None and node.key != key:
            node = node.next

        return node

    def get(self, key):
        return self.getNode(key).value

    def remove(self, key):
        node = self.getNode(key)
        if node.key is not None:
            self.deleteNode(node)
