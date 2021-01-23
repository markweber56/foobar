import math
import numpy as np
# foobar !!!! 1 2 3 are fastest !!!!!

def solution(grid):
    g = np.asarray(grid)
    fastest = g.shape[1] + g.shape[0] - 1
    tot = sum(sum(g))
    all_maps = [g]
    all_maps += [remap(g, i) for i in range(tot)]
    best = 401
    if tot <= min(g.shape):
        return fastest
    else:
        for m in all_maps:
            # print "TEST: ", m == g
            esc = Escape(m)
            esc.getgraph()
            nodes = esc.getmin()
            if nodes == fastest:
                return nodes
            elif nodes < best:
                best = nodes
    return best

class Escape:
    def __init__(self, test):
        self.visited = []
        self.graph = {}
        self.grid = test
        self.num_moves = 1
        self.rows = self.grid.shape[0]
        self.cols = self.grid.shape[1]
        self.ending = self.rows * self.cols - 1
        self.fin = False
        self.best = 401
        self.moves = [
            [0, 1],
            [0 , -1],
            [1, 0],
            [-1, 0]
        ]
        self.old_pos = []
        self.new_pos = []

    def get_xy(self, num):
        y = int(num / self.cols)
        x = num - self.cols * y
        return [x, y]

    def get_num(self, v):
        num = int(self.cols * v[1] + v[0])
        return num

    def get_pos(self, loc):
        s = self.get_xy(loc)
        ret = []
        for move in self.moves:
            pos = [s[0] + move[0], s[1] + move[1]]
            if (pos[0] >= 0 and pos[0] < self.cols) and \
                (pos[1] >= 0 and pos[1] < self.rows) and \
                (self.grid[pos[1]][pos[0]]) == 0:
                ret.append(self.get_num(pos))
        return ret

    def getgraph(self):
        pos = [0]
        while pos:
            s = pos.pop(0)
            if s not in self.visited:
                self.visited.append(s)
                new_pos = self.get_pos(s)
                self.graph[s] = new_pos
                pos += new_pos
        print self.graph
        return self.graph

    def getmin(self):
        self.old_pos = self.graph.pop(0)
        while self.graph and self.fin == False:
            while self.old_pos and self.fin == False:
                p = self.old_pos.pop(0)
                if p == self.ending:
                    self.fin = True;
                if p in self.graph:
                    self.new_pos += self.graph.pop(p)
            self.old_pos = self.new_pos
            self.new_pos = []
            self.num_moves += 1
        if self.fin:
            return self.num_moves
        return 401

def remap(g1, idx):
    g = g1.copy()
    loc = zip(*np.where(g == 1))[idx]
    g[loc[0]][loc[1]] = 0
    return g

if __name__ == '__main__':
        grid = [[0, 1, 1, 0], [1, 1, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
        grid = [[0, 0, 0, 0], [0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 0]]
        grid = [[0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
        grid = [
            [0, 1, 1, 0, 0 ,0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0]
        ]
        grid = [
            [0, 1, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 1, 0]
        ]
        print np.asarray(grid)
        s = solution(grid)
        print 'solution: ',s
