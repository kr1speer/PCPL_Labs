from lab_python_fp.gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):

        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()
        self._first_iteration = True

    def __next__(self):
        while True:
            item = next(self.items)

            if self.ignore_case and isinstance(item, str):
                key = item.lower()
            else:
                key = item
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self

def test_unique():
    print("Числа:")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for i in Unique(data1):
        print(i, end=' ')

    print("\n\nignore_case=False:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data2):
        print(i, end=' ')

    print("\n\nignore_case=True ")
    for i in Unique(data2, ignore_case=True):
        print(i, end=' ')

    print("\n\nГенератор:")
    data3 = gen_random(10, 1, 3)
    for i in Unique(data3):
        print(i)
