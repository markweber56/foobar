import os
import math
import json
os.system('clear')

class Escape:
    def __init__(self, test):
        self.num_moves = 1
        self.visited = []
        self._map = {}
        self.grid = test
        self.rows = len(test) # y direction
        self.cols = len(test[0]) # x direction
        self.crumbs = {}
        self.fastest = self.rows + self.cols - 1
        self.ending = self.rows * self.cols - 1
        self.best = 0
        self.moves = [
            [0, 1],
            [0 , -1],
            [1, 0],
            [-1, 0]
        ]

    def get_xy(self, num):
        y = int(math.floor(num / self.cols))
        return [num - self.rows * y, y]

    def get_num(self, v):
        return int(self.rows * v[1] + v[0])

    def get_pos(self, loc):
        s = self.get_xy(loc)
        ret = []
        for move in self.moves:
            pos = [s[0] + move[0], s[1] + move[1]]
            if (pos[0] >= 0 and pos[0] <= self.cols - 1) and \
                (pos[1] >= 0 and pos[1] <= self.rows - 1) and \
                (self.grid[pos[1]][pos[0]]) == 0:
                ret.append(self.get_num(pos))
        return ret

    def walk_util(self, s, visited):
        visited.add(s)
        # print s

        for idx, n in enumerate(self._map[s]):
            print 'node: ',s
            if n not in visited:
                if n == self.ending:
                    print "ENDED IN %d steps" % (len(visited) + 1)
                self.walk_util(n, visited)


        # for neighbor in


    def get_map(self):
        pos = [0]
        while pos:
            s = pos.pop(0)
            if s not in self.visited:
                self.visited.append(s)
                new_pos = self.get_pos(s)
                self._map[s] = new_pos
                pos += new_pos
        for k, v in self._map.items():
            print k,' : ',v
        return self._map

if __name__ == '__main__':
    grid = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
    grid = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
    for row in grid:
        print row
    escape = Escape(grid)
    _map = escape.get_map()
    escape.walk_util(0, set())
