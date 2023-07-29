# ID - 87729179
from collections import Counter


def games(game_condition, playing_field):
    if playing_field == '':
        return '0'
    result = 0
    for value in Counter(playing_field).values():
        if int(value) <= game_condition * 2:
            result += 1
    return result


if __name__ == '__main__':
    game_condition = int(input())
    convert_input = [x for x in range(4) for x in list(input()) if x != '.']
    row_game = ''.join(convert_input)
    print(games(game_condition, row_game))
