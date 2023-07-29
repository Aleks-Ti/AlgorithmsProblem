def combinations(comba):
    enter_keys = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
    }

    result = []

    def other(comba, n1=0, prefix=''):
        if len(comba) == n1:
            result.append(prefix)
            return
        for char in enter_keys[comba[n1]]:
            other(comba, n1 + 1, prefix + char)

    other(comba)
    return (' '.join(result))


if __name__ == '__main__':
    user_input = str(input())
    print(combinations(user_input))
