with open('input.txt', 'r') as f:
    lines = f.readlines()
    row_all = int(lines[0].rstrip()) - 1
    col_all = int(lines[1].rstrip()) - 1
    row_point = int(lines[-2].rstrip())
    col_point = int(lines[-1].rstrip())
    matrix = [x.split(' ') for x in lines[2:-2]]

result = []


def convert_to_int(asd):
    asd = int(asd)
    result.append(asd)


if row_point > 0:
    neighbor = (matrix[row_point - 1][col_point])  # вверх
    convert_to_int(neighbor)
if row_point < row_all:
    neighbor = (matrix[row_point + 1][col_point])  # вниз
    convert_to_int(neighbor)
if col_point > 0:
    neighbor = (matrix[row_point][col_point - 1])  # лево
    convert_to_int(neighbor)
if col_point < col_all:
    neighbor = (matrix[row_point][col_point + 1])  # право
    convert_to_int(neighbor)

convert = [str(x) for x in sorted(result)]
print((' '.join(convert)))
