class MyHashMap:

    def __init__(self):
        self.keys=[]
        self.values=[]

        """
        Initialize your data structure here.
        """


    def put(self, key, value):
        if key not in self.keys:
            self.keys.append(key)
            self.values.append(value)
        else:
            self.values[self.keys.index(key)]=value
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """


    def get(self, key):
        if key not in self.keys:
            return -1
        return self.values[self.keys.index(key)]
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """


    def remove(self, key):
        if key not in self.keys:
            return
        self.values.pop(self.keys.index(key))
        self.keys.remove(key)
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
