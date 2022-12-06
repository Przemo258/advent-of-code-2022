def get_elf_calories(list_from_elfs: str = '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000'):
    result = []
    elf_strings = list_from_elfs.split('\n\n')

    for elf_string in elf_strings:
        elf_list = elf_string.split('\n')
        elf_ints = list(map(int, elf_list))
        result.append((sum(elf_ints)))

    result.sort(reverse=True)
    return result


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        elf_calories = get_elf_calories(file.read())
        max_calories = elf_calories[0]
        top_3_calories = sum(elf_calories[:3])
        print(f'Elf with max calories has {max_calories} calories')
        print(f'Elfs with highest amount of calories (top 3) have {top_3_calories} calories in total')
