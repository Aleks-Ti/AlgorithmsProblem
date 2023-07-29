def big_number(array_len, array):

    for _ in range(array_len):
        for index_array in range(0, array_len - 1):
            CONTROL = array[index_array]
            CONTROOOOOL = array[index_array + 1]
            if int(array[index_array][0]) < int(array[index_array + 1][0]):
                array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]

            elif int(array[index_array][0]) == int(array[index_array + 1][0]):
                if len(array[index_array]) == 2 and len(array[index_array + 1]) == 2:
                    if int(array[index_array]) < int(array[index_array + 1]) and len(array[index_array]) == 2 and len(array[index_array + 1]) == 2:
                        array[index_array + 1], array[index_array] = array[index_array], array[index_array + 1]
                elif len(array[index_array]) > 1 and len(array[index_array + 1]) == 1:
                    if int(array[index_array][1]) == int(array[index_array + 1]):
                        continue
                    else:
                        if int(array[index_array][1]) < int(array[index_array + 1]):
                            array[index_array + 1], array[index_array] = array[index_array], array[index_array + 1]
                elif len(array[index_array + 1]) > 1 and len(array[index_array]) == 1:
                    if int(array[index_array]) == int(array[index_array + 1][1]):
                        continue
                    else:
                        if int(array[index_array]) < int(array[index_array + 1][1]):
                            array[index_array + 1], array[index_array] = array[index_array], array[index_array + 1]
                else:
                    if int(array[index_array]) > int(array[index_array + 1]) and (int(array[index_array]) == 10 or int(array[index_array]) == 10):
                        array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]
                    elif int(array[index_array]) < int(array[index_array + 1]) and (int(array[index_array]) == 10 or int(array[index_array]) == 10):
                        array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]

                    if int(array[index_array]) > int(array[index_array + 1]) and (int(array[index_array]) == 100 or int(array[index_array]) == 100):
                        array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]
                    elif int(array[index_array]) < int(array[index_array + 1]) and (int(array[index_array]) == 100 or int(array[index_array]) == 100):
                        array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]
                    if int(array[index_array]) > int(array[index_array + 1]) and (int(array[index_array]) == 1000 or int(array[index_array]) == 1000):
                        array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]
                    elif int(array[index_array]) < int(array[index_array + 1]) and (int(array[index_array]) == 1000 or int(array[index_array]) == 1000):
                        array[index_array], array[index_array + 1] = array[index_array + 1], array[index_array]

    return array


if __name__ == '__main__':
    array_len = 100
    array = [x for x in '82 468 941 181 287 861 291 515 263 424 470 620 954 894 565 69 148 587 823 57 730 389 921 1000 447 1000 748 104 831 943 174 24 340 1000 150 937 324 919 748 271 980 575 392 779 222 316 944 1000 160 501 319 436 26 828 348 211 825 857 486 1000 419 509 409 679 576 700 418 810 674 83 785 251 947 868 964 384 497 192 1000 998 756 649 269 290 197 30 95 796 642 980 474 122 443 707 839 213 1000 530 263 193'.split()]
    print(big_number(array_len, array))
