from magazine.Device import Device

device = Device()

with open('data/input.txt', 'r') as file:
    for line in file.readlines():
        commands = line.strip().split()
        if commands[0] == 'noop':
            device.noop()
        elif commands[0] == 'addx':
            device.add_x(int(commands[1]))

# part 1
print(f'The total of signal strengths is {device.total_signal_strength}')  # 14560
print('------------------------------------------------')
# part 2
print(device.img)  # EKRHEPUZ
