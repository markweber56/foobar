import math
import numpy as np
# foobar !!!! 1 2 3 are fastest !!!!!

def solution(grid):
    g = np.asarray(grid)
    fastest = g.shape[1] + g.shape[0] - 1
    print 'fastest: ',fastest
    best = 401
    tot = sum(sum(g))
    if tot <= min(g.shape) and False:
        return fastest
    else:
        all_maps = [g]
        all_maps += [remap(g, i) for i in range(tot)]
        for idx, m in enumerate(all_maps):
            print idx
            print m
        for m in all_maps:
            f = get_fast(m)
            print 'f: ',f
            if f == fastest:
                return fastest
            if f < best:
                print 'f is less than best'
                best = f
    print 'returning best: ',best
    return best

class Escape:
    def __init__(self, test):
        self.visited = []
        self.graph = {}
        self.grid = test
        self.rows = self.grid.shape[1]
        self.cols = self.grid.shape[0]
        self.ending = self.rows * self.cols - 1
        self.branches = [[0]]
        self.best = 401
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

    def walk(self, branch):
        for s in self.graph[branch[-1]]:
            if s not in branch:
                new_branch = branch + [s]
                if new_branch not in self.branches:
                    self.branches.append(new_branch)
                    if branch in self.branches:
                        self.branches.remove(branch)
                if s != self.ending:
                    self.walk(new_branch)

    def getgraph(self):
        pos = [0]
        while pos:
            s = pos.pop(0)
            if s not in self.visited:
                self.visited.append(s)
                new_pos = self.get_pos(s)
                self.graph[s] = new_pos
                pos += new_pos
        return self.graph

    def get_f(self):
        for b in self.branches:
            if self.ending in b and len(b) < self.best:
                self.best = len(b)
        return self.best

def remap(g1, idx):
    g = g1.copy()
    loc = zip(*np.where(g == 1))[idx]
    g[loc[0]][loc[1]] = 0
    return g

def get_fast(g):
    esc = Escape(g)
    esc.getgraph()
    esc.walk([0])
    # print 'branches: ',esc.branches
    return esc.get_f()

if __name__ == '__main__':
        # grid = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
        grid = [[0, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
        grid = [
            [0, 1, 1, 0, 0 ,0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 1],
            [0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0]
        ]
        grid = [
            [0, 1, 1],
            [1, 0, 1],
            [1, 0, 0]
            ]
        s = solution(grid)
        print np.asarray(grid)
        print 'solution: ',s
