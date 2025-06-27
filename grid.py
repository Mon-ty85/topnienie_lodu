from point import Point
from connection import Connection

class Grid:
    def __init__(self, n_size):
        self.n_size = n_size
        self.points = []
        self.connections = []

    def generate(self):
        self.points = []
        for i in range(self.n_size):
            row = []
            for j in range(self.n_size):
                p_point = Point(100+i*50 , 100+j*50)
                row.append(p_point)
            self.points.append(row)

        self.connections = []
        for i in range(self.n_size):
            for j in range(self.n_size):
                if j < self.n_size - 1:
                    self.connections.append(Connection(self.points[i][j], self.points[i][j + 1]))
                    self.points[i][j].line_num += 1
                    self.points[i][j + 1].line_num += 1
                if i < self.n_size - 1:
                    self.connections.append(Connection(self.points[i][j], self.points[i + 1][j]))
                    self.points[i][j].line_num += 1
                    self.points[i + 1][j].line_num += 1

    def update_active_points(self):
        p_list = []
        for pol in self.connections:
            if pol.check_broken():
                p_list.append(pol.p1)
                p_list.append(pol.p2)
        return p_list