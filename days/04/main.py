with open('input.txt', 'r') as file:
    contents = file.read()
    pairs = contents.split('\n')
    total_overlap = 0
    partial_overlap = 0
    for pair in pairs:
        r1, r2 = pair.split(',')
        n1, n2 = list(map(int, r1.split('-'))), list(map(int, r2.split('-')))
        s1, s2 = set(range(n1[0], n1[1] + 1)), set(range(n2[0], n2[1] + 1))

        if s1.intersection(s2) != set():
            partial_overlap += 1  # 933
        if s1.issubset(s2) or s2.issubset(s1):
            total_overlap += 1  # 584

    print(f'Total overlap: {total_overlap} elfs')
    print(f'Partial overlap: {partial_overlap} elfs')
