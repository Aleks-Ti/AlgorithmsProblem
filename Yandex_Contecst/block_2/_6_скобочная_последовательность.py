input_user = [x for x in '(())']
# input_user = [x for x in input()]


def is_correct_bracket_seq(array):
    char_dict = {
        '{': '}',
        '[': ']',
        '(': ')',
    }
    bad_char_dict = {
        '{': [']', ')'],
        '[': [')', '}'],
        '(': ['}', ']'],
    }
    char_error = ['}', ']', ')']

    if len(array) > 1 and len(array) % 2 == 0 and array[0] in char_dict:
        while True:
            for _ in range(len(array) - 1):
                if array == []:
                    print(True)
                    return True
                if array[0] in char_error:
                    print(False)
                    return False
                if (
                    array[1] != char_dict[array[0]]
                    and array[1] in bad_char_dict[array[0]]
                ):
                    print(False)
                    return False
                count = 1
                while True:
                    if count > len(array) - 1:
                        print(False)
                        return False
                    if count == 2 and char_dict[array[0]] == array[count]:
                        count += 1
                    if array[count] in char_dict:
                        count += 1
                    elif char_dict[array[0]] == array[count]:
                        del array[count]
                        del array[0]
                        break
                    else:
                        count += 1

            print(True)
            return True

    elif len(array) == 0:
        print(True)
    else:
        print(False)


is_correct_bracket_seq(input_user)
