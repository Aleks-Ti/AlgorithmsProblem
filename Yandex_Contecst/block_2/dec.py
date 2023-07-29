# ID - 88443015


class DequeIsFullError(Exception):
    pass


class DequeIsEmptyError(Exception):
    pass


class Deque:
    def __init__(self, list_qeue: list, max_queue: int):
        self.__list_qeue = list_qeue
        self.__max_queue = max_queue

    def push_back(self, value, size_qeue):
        if size_qeue == self.__max_queue:
            raise DequeIsFullError('error: stack is full')
        self.__list_qeue.append(value)

    def push_front(self, value, size_qeue):
        if size_qeue == self.__max_queue:
            raise DequeIsFullError('error: stack is full')
        self.__list_qeue.insert(0, value)

    def pop_front(self, size_qeue):
        if size_qeue == 0:
            raise DequeIsEmptyError('error: stack is empty')
        item = self.__list_qeue.pop(0)
        return item

    def pop_back(self, size_qeue):
        if size_qeue == 0:
            raise DequeIsEmptyError('error: stack is empty')
        item = self.__list_qeue.pop(-1)
        return item


def result_dek(command_list: list, max_queue: int):
    size_qeue = 0
    list_qeue = []
    ekz_stack = Deque(list_qeue, max_queue)
    for comm in command_list:
        command, *args = comm.split()
        if not args:
            try:
                result_action = getattr(ekz_stack, command)(
                    *args, size_qeue
                )
                if result_action is not None:
                    print(result_action)
                size_qeue -= 1
            except DequeIsEmptyError:
                print('error')
        else:
            try:
                result_action = getattr(ekz_stack, command)(*args, size_qeue)
                if result_action is not None:
                    print(result_action)
                size_qeue += 1
            except DequeIsFullError:
                print('error')


if __name__ == '__main__':
    len_list = int(input())
    max_queue = int(input())
    command_input = [x for x in range(len_list) for x in input().split('\n')]
    result_dek(command_input, max_queue)
