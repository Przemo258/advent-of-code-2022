from magazine.simulator import Simulator

simulator = Simulator(1000, 1000, 9)

with open('data/input.txt', 'r') as file:
    for line in file.readlines():
        commands = line.strip().split()
        direction, times = commands[0], int(commands[1])
        if direction == 'U':
            simulator.move_up(times)
        elif direction == 'D':
            simulator.move_down(times)
        elif direction == 'L':
            simulator.move_left(times)
        elif direction == 'R':
            simulator.move_right(times)
    simulator.print_game_board()
    
    # part 1
    print(f'The tail 1 was on {simulator.count_moves("1")} positions')  # 6642
    # part 2
    print(f'The tail 9 was on {simulator.count_moves("9")} positions')  # 2765

    # additional check :D # 2765
    total = 1
    for row in simulator.game_board:
        for cell in row:
            if '#' in cell:
                total += 1
    print(total)
