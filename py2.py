# Task 2.

# Option 1:
class CircularList1(object):
    def __init__(self, _list):
        """
        Initialization
        :param _list: List on numbers
        """
        self._mylist = _list

    def add_to_buffer(self, num):
        """
        Add new num to buffer
        :param num: Number
        """
        self._mylist.pop(0)
        self._mylist.append(num)

    def __repr__(self):
        """
        Return string representation
        """
        return self._mylist.__repr__()


mylist_2 = [13, 67, 33, 10]

my_crclist = CircularList1(mylist_2)

my_crclist.add_to_buffer(5)

print(my_crclist)


# Option 2.

class CircularList2(object):
    def __init__(self, size):
        """
        Initialization of index, size and list of numbers
        :param size: List size
        """
        self.index = 0
        self.size = size
        self._data = []

    def append(self, value):
        """
        Append an element
        :param value: Value to add
        """
        if len(self._data) == self.size:
            self._data[self.index] = value
        else:
            self._data.append(value)
        self.index = (self.index + 1) % self.size

    def __repr__(self):
        """Return string representation"""
        return self._data.__repr__()


my_crclist = CircularList2(size=5)

my_crclist.append(30)
my_crclist.append(10)
my_crclist.append(156)
my_crclist.append(435)
my_crclist.append(11)
my_crclist.append(33)

print(my_crclist)
