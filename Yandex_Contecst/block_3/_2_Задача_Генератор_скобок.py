def bracket_sequence(n1, n2, prefix=''):
    if n1 == 0 and n2 == 0:
        print(prefix)
    else:
        if n1 > 0:
            bracket_sequence(n1 - 1, n2, prefix + '(')
        if n1 < n2:
            bracket_sequence(n1, n2 - 1, prefix + ')')


if __name__ == '__main__':
    number = int(input())
    bracket_sequence(number, number)
