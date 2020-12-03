import itertools
import re

pattern = re.compile("(?P<min>[0-9]+)-(?P<max>[0-9]+)[ ](?P<c>[a-z])[:][ ](?P<pass>[0-9a-zA-Z]+)")

def part1():
    good_cnt = 0
    with open('input.txt', 'r') as input:
        for line in input.readlines():
            line = line.strip()
            #print(line)

            m = pattern.match(line)

            if m is None:
                print(f'Failed to process: {line}')
                break

            min_occ = int(m.group("min"))
            max_occ = int(m.group("max"))
            c = m.group("c")
            p = m.group("pass")

            #print(f'{min_occ} {max_occ} {c} {p}')

            occ = 0

            for t in p:
                if t == c:
                    occ = occ + 1

            if occ >= min_occ and occ <= max_occ:
                good_cnt = good_cnt + 1
            #print(good_cnt)

    print(good_cnt)

def part2():
    good_cnt = 0
    with open('input.txt', 'r') as input:
        for line in input.readlines():
            line = line.strip()
            #print(line)

            m = pattern.match(line)

            if m is None:
                print(f'Failed to process: {line}')
                break

            idx_1 = int(m.group("min"))
            idx_2 = int(m.group("max"))
            c = m.group("c")
            p = m.group("pass")

            #print(f'{idx_1} {idx_2} {c} {p}')

            idx_1_good = p[idx_1-1] == c
            idx_2_good = p[idx_2-1] == c

            #print(f'{idx_1_good} {idx_2_good}')
            
            if (idx_1_good ^ idx_2_good):
                good_cnt = good_cnt + 1

    print(good_cnt)

part1()
part2()
