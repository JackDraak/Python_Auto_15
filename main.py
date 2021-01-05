# Playing around with Python 3, continued:
# the game "Fifteen", for the console, a different approach.
# (C) 2021 Jack Draak

import random


class Game:
    def __init__(self, size):
        self.size = size
        tiles = []
        for label in set(range(1, size * size + 1)):
            tiles.append(label)
        self.tiles = tiles
        self.free_position_label = size * size
        self.tile_matrix = self.get_matrix()
        print(self.tiles)
        print(self.tile_matrix)

    def __repr__(self):
        print_string = str()
        position = 0
        for x in range(self.size):
            print_string += "\t"
            for y in range(self.size):
                label = self.tiles[position]
                if label is self.size * self.size:
                    print_string += "\t"
                else:
                    print_string += f"\t{self.tiles[position]}"
                position += 1
            print_string += "\n"
        print_string += str(self.solved())
        return print_string

    def get_matrix(self):
        matrix = []
        position = 0
        for x in range(self.size):
            row = []
            for y in range(self.size):
                row.append(self.tiles[position])
                position += 1
            matrix.append(row)
        return matrix

    def solved(self):
        position = 1
        for tile in self.tiles:
            if tile != position:
                return False
            position += 1
        return True

    def swap(self, a, b):
        self.tiles[a], self.tiles[b] = self.tiles[b], self.tiles[a]


if __name__ == '__main__':
    g = Game(4)
    print(g)
    g.swap(7, 3)
    print(g)
    g.swap(7, 3)
    print(g)

