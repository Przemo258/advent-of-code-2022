if __name__ == '__main__':
    # part 1
    with open('input.txt', 'r') as file:
        rucksacks = file.read().split('\n')
        total_sum = 0
        for rucksack in rucksacks:
            comp1, comp2 = set(rucksack[0:len(rucksack) // 2]), set(rucksack[len(rucksack) // 2:])
            in_both: set[str] = comp1.intersection(comp2)
            rucksack_sum = 0
            for item in in_both:
                priority = ord(item) - 65
                priority += 27 if item.isupper() else -31
                rucksack_sum += priority
            total_sum += rucksack_sum
        print(total_sum)
    # 7872

    # part 2
    with open('input.txt', 'r') as file:
        rucksacks = file.read().split('\n')
        total = 0
        for i in range(0, len(rucksacks), 3):
            group = [set(rucksacks[i]), set(rucksacks[i + 1]), set(rucksacks[i + 2])]
            common = group[0]
            for rucksack in group:
                common = common.intersection(rucksack)
            for item in common:
                priority = ord(item) - 65
                priority += 27 if item.isupper() else -31
                total += priority
        print(total)
    # 2497
