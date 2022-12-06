import re

# data = [['Z', 'N'], ['M', 'C', 'D'], ['P']]

data = [['B', 'S', 'V', 'Z', 'G', 'P', 'W'],
        ['J', 'V', 'B', 'C', 'Z', 'F'],
        ['V', 'L', 'M', 'H', 'N', 'Z', 'D', 'C'],
        ['L', 'D', 'M', 'Z', 'P', 'F', 'J', 'B'],
        ['V', 'F', 'C', 'G', 'J', 'B', 'Q', 'H'],
        ['G', 'F', 'Q', 'T', 'S', 'L', 'B'],
        ['L', 'G', 'C', 'Z', 'V'],
        ['N', 'L', 'G'],
        ['J', 'F', 'H', 'C']]

# move ? from ? to ?

with open('input.txt', 'r') as file:
    for line in file.readlines():
        clean = re.sub('move|from|to', '', line).split()
        inputs: list[int] = list(map(int, clean))
        inputs[1], inputs[2] = inputs[1] - 1, inputs[2] - 1
        moved = []
        for move in range(inputs[0]):
            moved.append(data[inputs[1]].pop())
        for item in reversed(moved):
            data[inputs[2]].append(item)
    result = []
    for item in data:
        result.append(item.pop())
    print(re.sub(r"[\W',]", '', str(result)))
