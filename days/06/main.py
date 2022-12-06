with open('input.txt', 'r') as file:
    data = list(file.read())
    # part 1 1912
    # last = [data[x] for x in range(0, 4)]
    # part 2 2122
    last = [data[x] for x in range(0, 14)]
    result = 0
    for i in range(4, len(data) - 1):
        if len(last) == len(set(last)):
            result = i
            break
        last.pop(0)
        last.append(data[i])
    print(result)
