# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            node = self.dict[key]
            self.delete(node)
            self.add_to_front(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.delete(node)
            self.add_to_front(node)
        else:
            node = Node(key, value)
            self.add_to_front(node)
            self.dict[key] = node

        if len(self.dict) > self.capacity:
            node_to_delete = self.tail.prev
            self.delete(node_to_delete)
            del self.dict[node_to_delete.key]  # type: ignore

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_front(self, node):
        node.next = self.head.next
        self.head.next.prev = node  # type: ignore
        node.prev = self.head
        self.head.next = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
