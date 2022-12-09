def get_matrix(file_name: str):
    data = []
    with open(file_name, 'r') as file:
        for raw in file.readlines():
            line = raw.strip()
            data.append(list(map(int, list(line))))
    return data


def check(index: int, array: list[int]) -> bool:
    value = array[index]
    for idx, number in enumerate(array):
        if idx >= index:
            return True
        if number >= value:
            return False
    return True


def scenic_score(index: int, array: list[int]) -> int:
    idx = index - 1
    value = array[index]
    score = 0
    while idx >= 0:
        score += 1
        if array[idx] >= value:
            break
        if array[idx] < value:
            idx -= 1
    return score


matrix = get_matrix('input.txt')
matrix_transposed = list(map(list, zip(*matrix)))
border_trees = 0
inside_trees = 0
max_scenic_score = 0

for i in range(len(matrix)):
    row = matrix[i]
    row_reversed = list(reversed(matrix[i]))

    for j in range(len(row)):
        length = len(row) - 1
        column = matrix_transposed[j]
        column_reversed = list(reversed(matrix_transposed[j]))

        if i == 0 or i == length or \
                j == 0 or j == length:
            border_trees += 1
            continue

        if check(j, row) or check(length - j, row_reversed) or \
                check(i, column) or check(length - i, column_reversed):
            inside_trees += 1

            current_score = scenic_score(j, row) * scenic_score(length - j, row_reversed)
            current_score *= scenic_score(i, column) * scenic_score(length - i, column_reversed)

            max_scenic_score = current_score if current_score > max_scenic_score else max_scenic_score

# part 1
print(f'There are {border_trees} border trees and {inside_trees} inside trees',
      f'a total of {border_trees + inside_trees}')  # 1676

# part 2
print(f'The max scenic score for this map is {max_scenic_score}')  # 313200
