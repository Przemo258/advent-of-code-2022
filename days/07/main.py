from magazine.file import File
from magazine.directory import Directory

root = Directory('/', None)
current_dir = root

with open('data/input.txt', 'r') as file:
    for raw in file.readlines():
        line = raw.strip()
        if line[0] == '$':
            user_input = line.split()
            if user_input[1] == 'cd':
                _, command, argument = line.split()
                if argument == '/':
                    current_dir = root
                elif argument == '..':
                    current_dir = current_dir.get_parent()
                else:
                    current_dir = current_dir.get_directory(argument)
        elif line[0] == 'd':
            _, dir_name = line.split()
            directory = Directory(dir_name, current_dir)
            current_dir.add_directory(directory)
        else:
            size, file_name = line.split()
            file = File(file_name, int(size), current_dir)
            current_dir.add_file(file)

    dirs = root.get_all_directories()

    # part 1
    total = 0
    for d in dirs:
        size = d.get_total_size()
        if size < 100000:
            total += size
    print(f'Total size of directories smaller than 100000 is {total}')

    # part 2
    free_space = 70000000 - root.get_total_size()
    required_space = 30000000 - free_space

    sorted_dirs = sorted(dirs, key=lambda i: i.get_total_size())
    filtered_dirs = list(filter(lambda i: i.get_total_size() >= required_space, sorted_dirs))
    directory_for_deletion = filtered_dirs[0]
    print(f'To get enough space for an update you should delete directory {directory_for_deletion}')
