number_1 = str(input())
number_2 = str(input())


def sum_binary(number_1, number_2):
    residue = 0
    result = []
    
    if len(number_1) > len(number_2):
        number_2 = '0' * (len(number_1) - len(number_2)) + number_2
    if len(number_1) < len(number_2):
        number_1 = '0' * (len(number_2) - len(number_1)) + number_1

    for index in range(len(number_1) - 1, -1, -1):
        if residue == 0:
            sum_num = int(number_1[index]) + int(number_2[index])
            if sum_num != 2 and sum_num != 3:
                residue = 0
                result.append(str(sum_num))
            elif sum_num == 2:
                residue = 1
                result.append(str(sum_num - 2))
            else:
                residue = 2
                result.append(str(sum_num - 3))
        else:
            sum_num = int(number_1[index]) + int(number_2[index]) + residue
            if sum_num == 3:
                residue = 1
                result.append(str(sum_num - 2))
            elif sum_num == 1:
                residue = 0
                result.append(str(sum_num))
            else:
                residue = 1
                result.append(str((sum_num - 2)))

    if residue == 2:
        result.append('1')
        result.append('1')
    if residue == 1:
        result.append('1')

    return ''.join((result[::-1]))


print(sum_binary(number_1, number_2))
