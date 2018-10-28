class MyHashSet:

    def __init__(self):
        self.keys=set()
        """
        Initialize your data structure here.
        """


    def add(self, key):
        self.keys.add(key)
        """
        :type key: int
        :rtype: void
        """


    def remove(self, key):
        if key in self.keys:
            self.keys.remove(key)
        """
        :type key: int
        :rtype: void
        """


    def contains(self, key):
        return key in self.keys
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
