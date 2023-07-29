# ID - 88442588


class StackIsEmptyError(Exception):
    pass


class Stack:
    def __init__(self):
        self.__result = []

    def pop(self):
        try:
            item = self.__result.pop(-1)
            return item
        except IndexError:
            raise StackIsEmptyError('error: stack is empty')

    def push(self, item: int):
        self.__result.append(item)
        return item


def calculator(data: list):
    stack = Stack()

    symbol_key = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y,
    }

    for char in data:
        if char in symbol_key:
            item_right = stack.pop()
            item_left = stack.pop()
            result_math = symbol_key[char](int(item_left), int(item_right))
            result = stack.push(result_math)
        else:
            result = stack.push(char)
    return result


if __name__ == '__main__':
    user_input = [x for x in input().split()]
    if len(user_input) == 1:
        print(user_input[0])
    else:
        print(calculator(user_input))
