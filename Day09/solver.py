data = [line.replace("\n", "") for line in open('input', 'r')]


class Knot:
    def __init__(self):
        self.history = []
        self.x = 0
        self.y = 0
        self.tail = None

    def get_history(self):
        h = []
        return [
            p for p in self.history if p not in h and (h.append(p) or True)
        ]

    def get_visited_positions(self):
        return len(self.get_history())

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Head(Knot):
    def move_down(self):
        self.y -= 1

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_up(self):
        self.y += 1

    def move(self, d):
        if d == "D":
            self.move_down()
        if d == "L":
            self.move_left()
        if d == "R":
            self.move_right()
        if d == "U":
            self.move_up()


class Tail(Knot):
    def follow(self, head):
        distance_x = head.get_x() - self.x
        distance_y = head.get_y() - self.y

        if abs(distance_x) == 2 and not distance_y:
            # horizontal move
            x_length = 1 if distance_x > 0 else -1
            self.x += x_length
        elif abs(distance_y) == 2 and not distance_x:
            # vertical move
            y_length = 1 if distance_y > 0 else -1
            self.y += y_length
        elif (abs(distance_y) == 2 and abs(distance_x) in (1, 2)) or \
             (abs(distance_x) == 2 and abs(distance_y) in (1, 2)):
            x_length = 1 if distance_x > 0 else -1
            self.x += x_length
            y_length = 1 if distance_y > 0 else -1
            self.y += y_length

        self.history.append([self.x, self.y])


class Rope:
    def __init__(self, length):
        self.knots = []
        self.length = length
        self.generate_rope()

    def add_knot(self, knot):
        self.knots.append(knot)

    def get_knots(self):
        return self.knots

    def generate_rope(self):
        h = Head()
        self.knots.append(h)
        for i in range(0, self.length):
            k = Tail()
            self.knots.append(k)

    def move_knots(self, d):
        for i in range(0, self.length+1):
            if i == 0:
                # head
                head = self.knots[i]
                head.move(d)
            else:
                # tail
                tail = self.knots[i]
                tail.follow(self.knots[i-1])


def get_visited_positions(r):
    for idx, move in enumerate(data):
        direction, steps = move.split(' ')
        for step in range(int(steps)):
            r.move_knots(direction)
    return r.knots[-1].get_visited_positions()


rope = Rope(1)
print(f"Visited positions 1: {get_visited_positions(rope)}")
rope = Rope(9)
print(f"Visited positions 2: {get_visited_positions(rope)}")
