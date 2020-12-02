import itertools

report_items = []

with open('input.txt', 'r') as input:
    for line in input.readlines():
        report_items.append(int(line.strip()))

def find_thingy(n):
    for r, combination in enumerate(itertools.combinations(report_items, n)):
        if sum(combination) == 2020:
            print(f'Lo! After examining {r} combinations, it was found that the sum of {combination} == 2020')

            product = 1
            
            for x in combination:
                product = product * x

            print(f'The product of {combination} = {product}')
            break
    else:
        print("Dun messed up")

find_thingy(2)
find_thingy(3)
