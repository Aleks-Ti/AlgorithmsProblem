def games(game_condition: int, row_play):
    if row_play == '':
        return '0'

    result = 0
    count_round = max(int(x) for x in row_play)
    count = 0
    for raund_n in range(1, count_round + 1):
        for button in row_play:
            if int(button) == raund_n:
                count += 1
        if count <= game_condition * 2 and count != 0:
            result += 1
            count = 0
        else:
            count = 0
    return result


if __name__ == '__main__':
    game_condition = int(input())
    convert_input = [x for x in range(4) for x in list(input()) if x != '.']
    row_game = ''.join(convert_input)
    print(games(game_condition, row_game))
