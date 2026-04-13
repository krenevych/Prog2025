class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self.current_position = len(self._collection) - 1 # поточна позиція ітератора у колекції

    def __next__(self):
        if self.current_position == - 1:
            raise StopIteration
        current_position = self.current_position
        self.current_position -= 1
        return self._collection[current_position]



class Collection:
    def __init__(self):
        self._lst = [] # список елементів, ПРИХОВАНЕ ПОЛЕ, НЕ ВИДИМЕ ЗЗОВНІ

    def add(self, element):
        self._lst.append(element)

    def __iter__(self):
        return Iterator(self._lst)

# main
if __name__ == '__main__':
    collection = Collection()
    collection.add(1)
    collection.add(2)
    collection.add(3)

    # for element in collection._lst:  # ТАК РОБИТИ НЕ МОЖНА, БО 1) ПОРУШЕННЯ ІНКАПСУЛЯЦІЇ 2) ТРЕБА ЗНАТИ, ЯК ВЛАШТОВАНА КОЛЕКЦІЯ
    #     print(element)

    for item in collection:
        print(item)