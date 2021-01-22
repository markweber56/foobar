import os
import math
os.system('clear')

# https://foobar.withgoogle.com/?eid=wZ1Sr

class Chess:
    def __init__(self):
        self.num_moves = 1
        self.visited = [False] * 64
        self.fin = False
        self.new_pos = []
        self.old_pos = []

        self.moves = [
            [-2, -1],
            [-2, 1],
            [2, -1],
            [2, 1],
            [-1, -2],
            [-1, 2],
            [1, -2],
            [1, 2]
        ]

    @staticmethod
    def get_xy(num):
        y = math.floor(num / 8.)
        return [num - 8 * y, y]

    @staticmethod
    def get_num(v):
        return int(8 * v[1] + v[0])

    def get_pos(self, start_pos, end_pos):
        new_pos = []
        for move in self.moves:
            pos = [start_pos[0] + move[0], start_pos[1] + move[1]]
            if pos == end_pos:
                self.fin = True
            if (pos[0] >= 0  and pos[0] <= 7) and (pos[1] >= 0 and pos[1] <= 7):
                if self.visited[self.get_num(pos)] == False:
                    self.visited[self.get_num(pos)] = True
                    new_pos.append(pos)

        return new_pos

    def get_min(self, start_num, end_num):
        start_pos = self.get_xy(start_num)
        end_pos = self.get_xy(end_num)
        self.visited[start_num] = True
        self.old_pos = self.get_pos(start_pos, end_pos)

        while self.fin == False:
            while self.old_pos and self.fin == False:
                p = self.old_pos.pop(0)
                self.new_pos += self.get_pos(p, end_pos)
            self.old_pos = self.new_pos
            self.new_pos = []
            self.num_moves += 1
        return self.num_moves


if __name__ == '__main__':
    start_num = 19
    end_num = 28
    num_moves = Chess().get_min(0 ,1)
    print 'num moves: ',num_moves
