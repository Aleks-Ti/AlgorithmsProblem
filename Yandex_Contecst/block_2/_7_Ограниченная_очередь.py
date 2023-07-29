class MyQueueSized:
    def __init__(self, list_qeue: list):
        self.list_qeue = list_qeue

    def push(self, item):
        self.list_qeue.append(item)

    def pop(self):
        if len(self.list_qeue) == 0:
            print('None')
        else:
            item = self.list_qeue.pop(0)
            print(item)

    def peek(self):
        if len(self.list_qeue) == 0:
            print('None')
        else:
            print(self.list_qeue[0])

    def size(self, size_qeue):
        print(size_qeue)


def result(command_list: list, max_queue: int):
    size_qeue = 0
    list_qeue = []

    for command in command_list:
        if command == 'peek':
            MyQueueSized(list_qeue).peek()
        elif command == 'size':
            MyQueueSized(list_qeue).size(size_qeue)
        elif command == 'pop':
            if size_qeue > 0:
                size_qeue -= 1
            MyQueueSized(list_qeue).pop()
        else:
            size_qeue += 1
            if size_qeue > max_queue:
                print('error')
                size_qeue -= 1
            else:
                command_list = command.split()
                item = int(command_list[1])
                MyQueueSized(list_qeue).push(item)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        number_len = int(lines[0].rstrip())
        max_queue = int(lines[1].rstrip())
        command_input = [x.rstrip('\n') for x in lines[2:]]
    result(command_input, max_queue)
