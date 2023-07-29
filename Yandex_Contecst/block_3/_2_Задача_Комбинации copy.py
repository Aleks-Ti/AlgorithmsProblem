def combinations(comba):
    enter_keys = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

    result = []

    def other(comba, n1=0, n2=0, n3=0, prefix=''):
        if comba == '':
            n1 = 0
            result.append(prefix + ' ')
            return
        for char in comba:
            if len(enter_keys[int(comba[0])]) != n1:
                other(comba[n2 + 1:], n1 + 1, n2, n3, prefix + enter_keys[int(char)][0])
            if n1 <= len(enter_keys[int(char)]):
                other(comba[n2 + 1:], n1 + 1, n2, n3, prefix + enter_keys[int(char)][1])
            if len(comba) == 1:
                other(comba[n2 + 1:], n1 + 1, n2, n3, prefix + enter_keys[int(char)][n2 + n1])

    return other(comba)


if __name__ == '__main__':
    user_input = '382'
    print(combinations(user_input))
