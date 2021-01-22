import os

os.system('clear')

def get_spot(v):
    max = sum(range(sum(v)))
    id = sum(range(sum(v) - 1)) + 1
    pos = [1, sum(v) - 1]
    if pos == v:
        return id
    while id <= max:
        id += 1
        pos[0] += 1
        pos[1] -= 1
        if pos == v:
            return id




if __name__ == '__main__':
    test_vars = {
        1: [1, 1],
        2: [1, 2],
        3: [2, 1],
        4: [1, 3],
        5: [2, 2],
        6: [3, 1],
        7: [1, 4],
        8: [2, 3],
        9: [3, 2],
        10: [4, 1],
        96: [5, 10]
    }
    for k, v in test_vars.items():
        print 'pos: ',v
        print 'id: ',k
        ans = get_spot(v)
        print 'ans: ',ans,'\n'
