class Head:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Head is on cords ({self.x},{self.y})'


class Tail(Head):
    was_on: list[(int, int)]
    name: str

    def __init__(self, x: int, y: int, name: str):
        super().__init__(x, y)
        self.was_on = []
        self.name = name

    def __str__(self):
        return f'Tail {self.name} is on cords ({self.x},{self.y}) and was on cords {self.was_on}'
