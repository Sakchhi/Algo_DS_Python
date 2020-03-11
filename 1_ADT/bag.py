"""
Bag ADT represents a container that stores a collection in which duplicate values are allowed
Items are stored individually, in no particular order, but should be comparable
Bag -- Constructor for empty bag
length -- Implements len
contains(item) -- Implements in operator
add(item)
remove(item) -- Remove and return item, raise exception if item not found
iterator -- Creates and returns iterator to iterate over collection of items
"""

from date import Date
class _BagIterator:
    def __init__(self, the_list):
        self._bag_items = the_list
        self._cur_item = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._cur_item < len(self._bag_items):
            item = self._bag_items[self._cur_item]
            self._cur_item += 1
            return item
        else:
            raise StopIteration

class Bag:
    def __init__(self):
        self.__items = list()

    def __len__(self):
        return len(self.__items)

    def add(self, item):
        self.__items.append(item)

    def __contains__(self, item):
        return item in self.__items

    def remove(self, item):
        assert item in self.__items, "The item must be in the bag"
        return self.__items.pop(self.__items.index(item))

    def __iter__(self):
        return _BagIterator(self.__items)



if __name__ == '__main__':
    my_bag = Bag()
    my_bag.add(Date(6,28,1991))
    my_bag.add(Date(2,27,1994))
    # my_bag.add("23")
    # my_bag.add("19")
    # my_bag.add("12")

    value = input("Guess a value contained in the bag: ")
    for value in my_bag:
        print(value)
