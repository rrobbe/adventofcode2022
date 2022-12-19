import math

data = [line.replace("\n", "") for line in open('input', 'r')]


class Item:
    def __init__(self, worry_level):
        self.worry_level = worry_level

    def get_worry_level(self):
        return self.worry_level

    def gets_bored(self, relief, super_test):
        if relief:
            self.worry_level = math.floor(self.worry_level // 3)
        else:
            self.worry_level = math.floor(self.worry_level % super_test)

    def is_divisible(self, test):
        if self.worry_level % test == 0:
            return True
        else:
            return False

    def set_new_worry_level(self, operation):
        old, operator, to_change = operation.split()
        if old == to_change:
            to_change = self.worry_level
        else:
            to_change = int(to_change)

        if operator == "*":
            self.worry_level *= to_change
        elif operator == "+":
            self.worry_level += to_change


class Monkey:
    def __init__(
        self,
        items,
        operation,
        test,
        to_monkey_if_true,
        to_monkey_if_false
    ):
        self.inspected_items = 0
        self.items = items
        self.operation = operation
        self.test = test
        self.to_monkey_if_true = to_monkey_if_true
        self.to_monkey_if_false = to_monkey_if_false

    def catch(self, item):
        self.items.append(item)

    def get_inspected_items(self):
        return self.inspected_items

    def get_items(self):
        return self.items

    def get_operation(self):
        return self.operation

    def get_test(self):
        return self.test

    def get_to_monkey_if_true(self):
        return self.to_monkey_if_true

    def get_to_monkey_if_false(self):
        return self.to_monkey_if_false

    def increase_inspected_items(self):
        self.inspected_items += 1


def read_data():
    with open("input", "r") as f:
        return [
            monkey.split("\n") for monkey in f.read().strip().split("\n\n")
        ]


def read_monkeys(data):
    monkeys = []
    for idx, monkey_data in enumerate(data):
        items = []
        operation = monkey_data[2].split(" = ")[1]
        test = int(monkey_data[3].split()[-1])
        for worry_level in (
            monkey_data[1].split(":")[1].replace(" ", "").split(",")
        ):
            items.append(
                Item(
                    worry_level=int(worry_level),
                )
            )

        to_monkey_if_true = int(monkey_data[4].split()[-1])
        to_monkey_if_false = int(monkey_data[5].split()[-1])
        monkeys.append(
            Monkey(
                items=items,
                operation=operation,
                test=test,
                to_monkey_if_true=to_monkey_if_true,
                to_monkey_if_false=to_monkey_if_false
            )
        )
    return monkeys


def process_round(monkeys, relief, super_test):
    for monkey in monkeys:
        items = monkey.get_items()
        items.reverse()
        while len(items):
            item = items.pop()
            monkey.increase_inspected_items()
            item.set_new_worry_level(monkey.get_operation())
            item.gets_bored(relief, super_test)
            if item.is_divisible(monkey.get_test()):
                monkeys[monkey.get_to_monkey_if_true()].catch(item)
            else:
                monkeys[monkey.get_to_monkey_if_false()].catch(item)


def process_rounds(number_of_rounds, relief):
    monkeys = read_monkeys(read_data())

    super_test = 1
    if not relief:
        test_values = []
        for monkey in monkeys:
            test_values.append(monkey.get_test())
        for test in test_values:
            super_test *= test

    for r in range(1, number_of_rounds+1):
        process_round(monkeys, relief, super_test)

    return monkeys


def get_monkey_business_level(number_of_rounds, relief):
    monkeys = process_rounds(number_of_rounds, relief)

    inspected_items = []
    for monkey in monkeys:
        inspected_items.append(monkey.get_inspected_items())
    return math.prod(sorted(inspected_items, reverse=True)[:2])


print(f"Calculate monkey business level (part 1): {get_monkey_business_level(20, True)}")
print(f"Calculate monkey business level (part 2): {get_monkey_business_level(10000, False)}")
