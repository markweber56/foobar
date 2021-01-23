import numpy as np
import os

def cl():
    os.system('clear')

class Geom:
    def __init__(self, shp):
        self.shp = shp
        self.cols = self.get_columns()
        self.rows = self.get_rows()


    def get_columns(self):
        cols = self.shp.shape[1]
        print '%d columns' % cols
        return cols

    def get_rows(self):
        rows = self.shp.shape[0]
        print '%d rows' % rows
        return rows

    def get_num(self, v):
        x = v[0]
        y = v[1]
        num = y * self.cols + x
        print 'loc: ',v
        print 'num: ',num
        return num

    def get_xy(self, num):
        y = int(num / self.cols)
        x = num - self.cols * y
        v = [x, y]
        print 'v: ',v
        return v

if __name__ == '__main__':
    grid = [
        [0, 1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10, 11]
    ]
    g = np.asarray(grid)
    print g
