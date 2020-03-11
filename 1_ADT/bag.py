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

    def __iter__(self, item):
        pass


if __name__ == '__main__':
    my_bag = Bag()
    my_bag.add(19)
    my_bag.add(74)
    my_bag.add(23)
    my_bag.add(19)
    my_bag.add(12)

    value = int(input("Guess a value contained in the bag: "))
    if value in my_bag:
        print("Bag contains the value", value)
    else:
        print("The bag does not contain the value", value)