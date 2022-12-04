import string

data = [line.strip() for line in open('input', 'r')]
priorities_1 = 0


def generate_mapper():
    m = {}
    for x, y in zip(range(1, 27), string.ascii_lowercase):
        m[y] = x
    for x, y in zip(range(27, 53), string.ascii_uppercase):
        m[y] = x
    return m


def split_to_rucksacks(items, chunk_size):
    return [items[i: i + chunk_size] for i in range(0, len(items), chunk_size)]


def find_duplicates(items):
    items1 = items[0]
    items2 = items[1]
    try:
        items3 = items[2]
    except Exception as e:
        items3 = []
    if len(items3) == 0:
        d = list(set(items1).intersection(items2))
    else:
        d = list(set(items1).intersection(items2, items3))
    return d


def get_priorities_1():
    priorities = 0
    for rucksack in data:
        chunk_size = int(len(rucksack) / 2)
        rucksack = split_to_rucksacks(rucksack, chunk_size)
        duplicates = find_duplicates(rucksack)
        for duplicate in duplicates:
            priorities += mapper[duplicate]
    return priorities


def get_priorities_2():
    priorities = 0
    chunk_size = 3
    grouped_elves = split_to_rucksacks(data, chunk_size)
    for group_of_elves in grouped_elves:
        duplicates = find_duplicates(group_of_elves)
        for duplicate in duplicates:
            priorities += mapper[duplicate]
    return priorities


mapper = generate_mapper()
print(f"priorities_1: {get_priorities_1()}")
print(f"priorities_2: {get_priorities_2()}")
