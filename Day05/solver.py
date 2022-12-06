import re

data = [line.replace("\n", "") for line in open('input', 'r')]
crates = []
instructions = []


def read_data():
    chunk_size = 4
    raw_crates = []
    max_stacks = 0

    # read data and split crates from instructions
    for line in data:
        if "[" in line:
            crates_in_line = int((len(line)+1)/4)
            if crates_in_line > max_stacks:
                max_stacks = crates_in_line
            raw_crates.append(line)
        if line.startswith('1') or line == "":
            continue
        if line.startswith("move"):
            instructions.append(line)

    # fill empty spots compared to highest crate
    for rc in raw_crates:
        stacks_in_line = [
            rc[i:i+chunk_size] for i in range(0, len(rc), chunk_size)
        ]
        nr_of_stacks = len(stacks_in_line)
        if nr_of_stacks < max_stacks:
            extra_stacks = max_stacks - nr_of_stacks
            for i in range(0, extra_stacks):
                stacks_in_line.append("    ")
        crates.append(stacks_in_line)


def build_stacks_grid(s):
    stacks = []
    width = len(s[0])
    # initiate multi dim array
    for i in range(0, width):
        stacks.append([])
    # fill rotated array: read horizontal, fill vertical (stacked)
    for row in reversed(s):
        for idx, c in enumerate(row):
            if c.strip() != '':
                stacks[idx].append(c.strip())
    return stacks


def execute_instructions(stacks, crane_type):
    for i in instructions:
        nr_of_moves = int(i.split()[1])
        from_pos = int(i.split()[3])-1
        to_pos = int(i.split()[5])-1
        if crane_type == "9001":
            tmp_stack = []
            for move in range(0, nr_of_moves):
                tmp_stack.append(stacks[from_pos].pop())
            # reverse tmp stack to keep the original order
            tmp_stack.reverse()
            for t_s in tmp_stack:
                stacks[to_pos].append(t_s)
        else:
            for move in range(0, nr_of_moves):
                crate = stacks[from_pos].pop()
                stacks[to_pos].append(crate)
    return stacks


def get_solution(stacks):
    solutions = []
    for s in stacks:
        solutions.append(re.findall(r'\[(.*?)\]', ''.join(s))[-1])
    return ''.join(solutions)


read_data()

stacks_1 = build_stacks_grid(crates)
stacks_2 = build_stacks_grid(crates)
stacks_1 = execute_instructions(stacks_1, "9000")
stacks_2 = execute_instructions(stacks_2, "9001")

print(f"solution 1: {get_solution(stacks_1)}")
print(f"solution 2: {get_solution(stacks_2)}")
