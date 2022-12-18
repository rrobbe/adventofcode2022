import math

data = [line.replace("\n", "") for line in open('input', 'r')]


class Register:
    def __init__(self):
        self.cycles = 0
        self.marker = 20
        self.signals = []
        self.value = 1

    def get_cycles(self):
        return self.cycles

    def get_value(self):
        return self.value

    def raise_value(self, value):
        self.cycles += 1
        if self.cycles == self.marker:
            s = Signal(self.cycles, self.value)
            self.signals.append(s)
            self.marker += 40
        self.value += value

    def sum_of_signal_strengths(self):
        total = 0
        for signal in self.signals:
            total += signal.get_strength()
        return total


class Signal:
    def __init__(self, marker, value):
        self.strength = marker * value

    def get_strength(self):
        return self.strength


class CRT:
    def __init__(self, width, height):
        self.pixels = []

    def draw_pixel(self):
        cycle = register.get_cycles()
        value = register.get_value()
        sprite_start = value - 1
        sprite_stop = sprite_start + 3
        if sprite_start < 0:
            sprite_start + 40
        if sprite_stop < 0:
            sprite_stop + 40
        sprite_range = range(sprite_start, sprite_stop)
        row_number = math.floor(cycle / 40)
        cycle_pixel = cycle - (row_number * 40)
        if cycle_pixel in [*sprite_range]:
            self.pixels.append('#')
        else:
            self.pixels.append('.')

    def print(self):
        crt_rows = [self.pixels[p:p+40] for p in range(0, len(self.pixels), 40)]
        for row_pixels in crt_rows:
            print(''.join(row_pixels))


register = Register()
crt = CRT(40, 6)
for instruction in data:
    instruction = instruction.split(' ')
    if instruction[0] == "noop":
        crt.draw_pixel()
        register.raise_value(value=0)
    if instruction[0] == "addx":
        v = 0
        for i in range(0, 2):
            crt.draw_pixel()
            if i == 1:
                v = int(instruction[1])
            register.raise_value(value=v)

print(f"Sum of signal strengths: {register.sum_of_signal_strengths()}")
print(f"Print CRT - Read the 8 capital letters:")
crt.print()
