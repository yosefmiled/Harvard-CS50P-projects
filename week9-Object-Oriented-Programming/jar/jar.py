class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪"*self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies")
        self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError("Not enough cookies")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError ("Capacity cannot be negative")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value > self._capacity or value < 0:
            raise ValueError ("The number of cookies is over/under the capacity of the jar")
"""
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError ("Wrong capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size *"🍪"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError("Exceed capacity")
        if self.size + n > self.capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self.size < n :
            raise ValueError("There are less cookies than asked to remove")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
"""
