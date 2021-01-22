import os

class Tree:
    def __init__(self):
        self.branches = [['a']]
        self.num_calls = 0
        self.graph = {
            'a': ['b'],
            'b': ['a', 'c', 'd'],
            'c': ['b', 'e', 'f'],
            'd': ['b', 'g', 'h'],
            'e': ['c'],
            'f': ['c', 'i'],
            'g': ['d', 'i'],
            'h': ['d'],
            'i': ['f', 'g']
        }

    def walk(self, branch):
        self.num_calls += 1
        if self.num_calls > 10:
            return
        print 'head: ',branch[-1]
        print 'nodes: ',self.graph[branch[-1]]
        for s in self.graph[branch[-1]]:
            if s not in branch:
                new_branch = branch + [s]
                if new_branch not in self.branches:
                    self.branches.append(new_branch)
                    if branch in self.branches:
                        self.branches.remove(branch)
                if s != 'i':
                    self.walk(new_branch)

if __name__ == '__main__':
    os.system('clear')
    tree = Tree()
    tree.walk(['a'])
    print tree.branches
