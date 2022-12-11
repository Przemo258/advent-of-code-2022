class Device:
    clock: int
    register_x: int
    total_signal_strength: int
    width: int
    height: int
    img: str

    def __init__(self):
        self.clock = 1
        self.register_x = 1
        self.total_signal_strength = 0
        self.img = ''

    def tick(self):
        if (self.clock - 20) % 40 == 0:
            self.total_signal_strength += self.clock * self.register_x

        reminder = (self.clock - 1) % 40
        if reminder == 0 and self.clock != 0:
            self.img += '\n'
        if reminder == self.register_x - 1 or reminder == self.register_x or reminder == self.register_x + 1:
            self.img += '#'
        else:
            self.img += '.'

        self.clock += 1

    def noop(self):
        self.tick()

    def add_x(self, number: int):
        for _ in range(2):
            self.tick()
        self.register_x += number
