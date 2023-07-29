number = int(input())
# tsil = stdin.read().rstrip('\n').split('\n')
# tsil = [
#     'pop',
#     'pop',
#     'push 4',
#     'push -5',
#     'push 7',
#     'pop',
#     'pop',
#     'get_max',
#     'pop',
#     'get_max',
# ]

tsil = [
    'get_max',
    'push -6',
    'pop',
    'pop',
    'get_max',
    'push 2',
    'get_max',
    'pop',
    'push -2',
    'push -6',
]

# tsil = [
#     'push 1',
#     'push 3',
#     'push 1',
#     'push 3',
#     'push 3',
#     'pop',
#     'get_max',
#     'pop',
#     'get_max',
#     'pop',
#     'get_max',
#     'pop',
#     'get_max',
# ]


class Stack:
    number_max: int

    def __init__(self, items, max_item):
        self.items = items
        self.max_item = max_item

    def push(self, item):
        if len(self.items) == 0:
            self.max_item.append(item)
        if item >= self.max_item[-1]:
            self.max_item.append(item)
        self.items.append(item)

    def pop(self):
        if not self.items:
            print('error')
            return None
        item = self.items.pop()
        if item == self.max_item[-1]:
            del self.max_item[-1]
        return item

    def get_max(self):
        if len(self.items) == 0:
            print('None')
        else:
            print((self.max_item[-1]))


def asd(asd: list):
    max_item = []
    result = []
    for command in tsil:
        if command == 'get_max':
            Stack(result, max_item).get_max()
        elif command == 'pop':
            Stack(result, max_item).pop()
        else:
            command_list = command.split()
            item = int(command_list[1])
            Stack(result, max_item).push(item)


asd(tsil)
