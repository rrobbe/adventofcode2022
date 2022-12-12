data = [line.replace("\n", "") for line in open('input', 'r')]
grid_trees = []
for line in data:
    grid_trees.append(list(line))
max_rows = len(grid_trees)
max_columns = len(grid_trees[0])


def generate_visible_grid():
    g_v = []
    for r in range(0, max_rows):
        g_v.append([])
        for c in range(0, max_columns):
            g_v[r].append(0)
    return g_v


def is_tree_visible(pos, trees, reverse=False):
    if reverse:
        enum_trees = reversed(list(enumerate(trees)))
        trees_from_edge = [idx for idx, tree in enum_trees if idx > pos]
    else:
        enum_trees = enumerate(trees)
        trees_from_edge = [idx for idx, tree in enum_trees if idx < pos]

    is_visible = True
    if pos == 0 or pos == len(trees)-1:
        # edge tree
        return is_visible
    else:
        height_of_tree_from_current_pos = trees[pos]
        height_of_neighbours = []
        for tree in trees_from_edge:
            height_of_neighbours.append(trees[tree])
        if not all(
            height_of_tree_from_current_pos > h for h in height_of_neighbours
        ):
            is_visible = False
        return is_visible


def mark_visible_tree(r, c):
    grid_visible[r][c] = 1


def get_number_of_visible_trees(g):
    total = 0
    for r in g:
        total += len([t for t in r if t == 1])
    return total


def calculate_scenic_score(r, c):
    score = [0, 0, 0, 0]

    tree_height = grid_trees[r][c]
    tree_down = r + 1
    tree_left = c - 1
    tree_right = c + 1
    tree_up = r - 1

    view_ok = True
    while tree_left >= 0 and view_ok:
        score[0] += 1
        if grid_trees[r][tree_left] < tree_height:
            tree_left -= 1
        else:
            view_ok = False

    view_ok = True
    while tree_right < max_columns and view_ok:
        score[1] += 1
        if grid_trees[r][tree_right] < tree_height:
            tree_right += 1
        else:
            view_ok = False

    view_ok = True
    while tree_up >= 0 and view_ok:
        score[2] += 1
        if grid_trees[tree_up][c] < tree_height:
            tree_up -= 1
        else:
            view_ok = False

    view_ok = True
    while tree_down < max_rows and view_ok:
        score[3] += 1
        if grid_trees[tree_down][c] < tree_height:
            tree_down += 1
        else:
            view_ok = False
    return score[0] * score[1] * score[2] * score[3]


# generate grid_visible with visibility = 0
grid_visible = generate_visible_grid()

# mark visible trees
for r in range(0, max_rows):
    # horizontal
    range_of_trees = range(0, max_columns)
    for c in range_of_trees:
        if is_tree_visible(c, grid_trees[r]):
            mark_visible_tree(r, c)
    # horizontal - reverse
    range_of_trees = list(range(max_columns, -1, -1))
    del range_of_trees[0]
    for c in range_of_trees:
        if is_tree_visible(c, grid_trees[r], reverse=True):
            mark_visible_tree(r, c)

for c in range(0, max_columns):
    # vertical
    trees_column = []
    for r in range(0, max_rows):
        trees_column.append(grid_trees[r][c])
    for r in range(0, max_rows):
        if is_tree_visible(r, trees_column):
            mark_visible_tree(r, c)
    # vertical - reverse
    trees_column = []
    for r in range(0, max_rows):
        trees_column.append(grid_trees[r][c])
    range_of_trees = list(range(max_rows, -1, -1))
    del range_of_trees[0]
    for r in range_of_trees:
        if is_tree_visible(r, trees_column, reverse=True):
            mark_visible_tree(r, c)

top_scenic_score = 0
for r_idx in range(0, max_rows):
    for c_idx in range(0, max_columns):
        top_scenic_score = max(
            top_scenic_score, calculate_scenic_score(r_idx, c_idx)
        )

print(f"Number of visible trees: {get_number_of_visible_trees(grid_visible)}")
print(f"Top scenic score: {top_scenic_score}")
