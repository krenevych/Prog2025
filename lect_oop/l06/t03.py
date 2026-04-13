class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self.current_position = 0 # поточна позиція ітератора у колекції

    def __next__(self):
        try:
            current_position = self.current_position
            self.current_position += 1
            return self._collection[current_position]
        except IndexError:
            raise StopIteration


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

    # for item in collection:
    iterator = iter(collection)
    # elem = next(iterator)
    # print(elem)
    # elem = next(iterator)
    # print(elem)
    # elem = next(iterator)
    # print(elem)
    # elem = next(iterator)
    # print(elem)
    while True:
        try:
            elem = next(iterator)
            print(elem)
        except StopIteration:
            break
    #         ||
    for elem in collection:
        print(elem)