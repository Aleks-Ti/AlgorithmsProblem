# from sys import stdin

number = int(input())
# tsil = stdin.read().rstrip('\n').split('\n')
# tsil = [
#     'get_max',
#     'push 7',
#     'pop',
#     'push -2',
#     'push -1',
#     'pop',
#     'get_max',
#     'get_max',
# ]

tsil = [
    'get_max',
    'pop',
    'pop',
    'pop',
    'push 10',
    'get_max',
    'push -9',
]


class Stack:
    def __init__(self, items: list):
        self.items = items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print('error')
        else:
            self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
        else:
            print(max(self.items))


result = []
for command in tsil:
    if command == 'get_max':
        Stack(result).get_max()
    elif command == 'pop':
        Stack(result).pop()
    else:
        command_list = command.split()
        item = int(command_list[1])
        Stack(result).push(item)
