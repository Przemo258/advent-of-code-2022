import os
from typing import Union
import math
from .Other import Head, Tail


class Simulator:
    game_board: list[list[list[str]]]
    width: int
    height: int
    head = Head
    tails = list[Tail]
    last_tail_name: str

    def __init__(self, width: int, height: int, parts: int = 1):
        start_x, start_y = width // 2, height // 2
        self.width = width
        self.height = height
        self.game_board = []
        self.head = Head(start_x, start_y)
        for i in range(height):
            row = []
            for j in range(width + 1):
                row.append(['.'])
            self.game_board.append(row)
        start_array = self.game_board[start_y][start_x] = ['H']
        self.tails = []
        for i in range(parts):
            name = str(i + 1)
            self.tails.append(Tail(start_x, start_y, name))
            start_array.append(name)
        self.last_tail_name = str(parts)

    def print_game_board(self):
        print()
        for row in self.game_board:
            for item in row:
                print(item[0], end='')
            print('')
        print('\n------------------------------------------------------------------------------------------')

    def set_symbol(self, part: Union[Head, Tail]):

        if type(part) == Head:
            symbols = self.game_board[self.head.y][self.head.x]
            if 'H' not in symbols:
                symbols.insert(0, 'H')
        elif type(part) == Tail:
            symbols = self.game_board[part.y][part.x]
            if 'H' in symbols and part.name not in symbols:
                symbols.insert(symbols.index('H'), part.name)
            elif 'T' not in symbols:
                symbols.insert(0, part.name)

    def remove_symbol(self, part: Union[Head, Tail]):
        if type(part) == Head:
            symbols = self.game_board[self.head.y][self.head.x]
            if 'H' in symbols:
                symbols.remove('H')
        if type(part) == Tail:
            symbols = self.game_board[part.y][part.x]
            if part.name in symbols:
                symbols.remove(part.name)
            if part.name == self.last_tail_name:
                if len(symbols) > 0:
                    symbols[-1] = '#'
                else:
                    symbols.append('#')

    def move_up(self, moves: int = 1):
        for i in range(moves):
            if self.head.y > 0:
                self.remove_symbol(self.head)
                self.head.y -= 1
                self.set_symbol(self.head)
                for tail in self.tails:
                    self.update_tails()

    def move_down(self, moves: int = 1):
        for i in range(moves):
            if self.head.y < self.height - 1:
                self.remove_symbol(self.head)
                self.head.y += 1
                self.set_symbol(self.head)
                self.update_tails()

    def move_left(self, moves: int = 1):
        for i in range(moves):
            if self.head.x > 0:
                self.remove_symbol(self.head)
                self.head.x -= 1
                self.set_symbol(self.head)
                self.update_tails()

    def move_right(self, moves: int = 1):
        for i in range(moves):
            if self.head.x < self.width:
                self.remove_symbol(self.head)
                self.head.x += 1
                self.set_symbol(self.head)
                self.update_tails()

    def update_tail(self, previous: Union[Head, Tail], tail: Tail):
        distance = math.sqrt(((previous.x - tail.x) ** 2) + ((previous.y - tail.y) ** 2))
        if distance >= 2:
            if (tail.x, tail.y) not in tail.was_on:
                tail.was_on.append((tail.x, tail.y))
            self.remove_symbol(tail)

            if tail.y > 0 and tail.y > previous.y:
                # move up
                tail.y -= 1
            elif tail.y < self.height and tail.y < previous.y:
                # move down
                tail.y += 1

            if tail.x > 0 and tail.x > previous.x:
                # move left
                tail.x -= 1
            elif tail.x < self.width and tail.x < previous.x:
                # move right
                tail.x += 1

            self.set_symbol(tail)

    def update_tails(self):
        previous_tail = self.head
        for idx, tail in enumerate(self.tails):
            self.update_tail(previous_tail, tail)
            previous_tail = tail

    def count_moves(self, tail_name: str = '1'):
        total = 1
        current = None
        for tail in self.tails:
            if tail.name == tail_name:
                current = tail
        if current is None:
            raise AttributeError('There is no such tail in tails')
        for _ in current.was_on:
            total += 1
        return total
