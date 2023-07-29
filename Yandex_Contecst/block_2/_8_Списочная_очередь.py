class MyQueue:
    def __init__(self, list_qeue: list, size_qeue=0):
        self.list_qeue = list_qeue
        self.size_qeue = size_qeue

    def get(self):
        print(self.list_qeue[0])
        del self.list_qeue[0]

    def put(self, item):
        self.list_qeue.append(item)

    def size(self, size_qeue):
        print(size_qeue)


def result(command_list: list, number_len: int):
    size_qeue = 0
    list_qeue = []

    for command in command_list:
        if command == 'size':
            MyQueue(list_qeue).size(size_qeue)
        elif command == 'get':
            if size_qeue != 0:
                MyQueue(list_qeue).get()
                size_qeue -= 1
            else:
                print('error')
        else:
            size_qeue += 1
            command_list = command.split()
            item = int(command_list[1])
            MyQueue(list_qeue, size_qeue).put(item)


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        number_len = int(lines[0].rstrip())
        command_input = [x.rstrip('\n') for x in lines[1:]]
    result(command_input, number_len)
