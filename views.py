import pygame as pg
import numpy as np
from energy_el import Energy_el
from grid import Grid
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Views:
    def __init__(self, sets):
        pg.init()
        self.setting = sets
        self.screen = pg.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pg.display.set_caption("Ice_melting")
        self.grid = Grid(self.setting.n_size)
        self.en_el = [Energy_el(0, 0) for _ in range(self.setting.l_ele)]
        self.clock = pg.time.Clock()
    
    def reset(self, ennn):
        ennn.sss = 0

        if self.setting.option == 1:
            direction = 1
        elif self.setting.option == 2:
            direction = np.random.choice([1, 2])
        elif self.setting.option == 3:
            direction = np.random.choice([1, 2, 3])
        elif self.setting.option == 4:
            direction = np.random.choice([1, 2, 3, 4])

        if direction == 1:
            ennn.x = 200+self.setting.n_size*50
            ennn.y = np.random.randint(200+self.setting.n_size*50)
            ennn.up = False
            ennn.right = True
            ennn.left = False
            ennn.down = False
        elif direction == 2:
            ennn.x = np.random.randint(200+self.setting.n_size*50)
            ennn.y = 0
            ennn.up = True
            ennn.right = False
            ennn.left = False
            ennn.down = False
        elif direction == 3:
            ennn.x = 0
            ennn.y = np.random.randint(200+self.setting.n_size*50)
            ennn.up = False
            ennn.right = False
            ennn.left = True
            ennn.down = False
        elif direction == 4:
            ennn.x = np.random.randint(200+self.setting.n_size*50)
            ennn.y = 200+self.setting.n_size*50
            ennn.up = False
            ennn.right = False
            ennn.left = False
            ennn.down = True

    def propagate_energy(self, point, force_x, force_y, visited, damping=0.8):
        if point in visited or (abs(force_x) < 0.01 and abs(force_y) < 0.01):
            return

        visited.add(point)
        point.move = True
        point.osc_force_x += force_x
        point.osc_force_y += force_y

        for conn in self.grid.connections:
            if conn.broken:
                continue
            next_point = None
            if conn.p1 == point:
                next_point = conn.p2
            elif conn.p2 == point:
                next_point = conn.p1
            if next_point and next_point not in visited:
                self.propagate_energy(
                    next_point,
                    force_x * damping,
                    force_y * damping,
                    visited,
                    damping
                )

    def _start(self):
        self.grid.generate()
        for eee in self.en_el:
            self.reset(eee)
        lista1 =[]
        lista2 = []
        mimi = 0
        run = True
        ts = time.time()
        while run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

            t = (pg.time.get_ticks() / 700) % 1000

            self.screen.fill(self.setting.black)

            positions = {}
            for eee in self.en_el:
                if eee.hhh == 0: 
                    eee.los1 = np.random.uniform(-1,1)
                eee.hhh += 1

                en_x, en_y = eee.update_position(ll=eee.los1)
                positions[eee] = (en_x, en_y)
                pg.draw.rect(self.screen, self.setting.green, (en_x - 10, en_y - 10, 20, 20))

            hit = False
            for row in self.grid.points:
                for pp in row:
                    if not hit:
                        for eee in self.en_el:
                            en_x, en_y = positions[eee]
                            result = pp.collide(en_x, en_y, eee, self.setting)
                            if result:
                                hit = True
                                damping = 0.8
                                force_x = result[1] / pp.line_num * damping
                                force_y = result[2] / pp.line_num * damping
                                

                                self.propagate_energy(pp, force_x, force_y, visited=set(), damping=0.8)

                                self.reset(eee)
                                eee.hhh = 0

                    pp.update_position(t)
                    pg.draw.rect(self.screen, self.setting.red, (pp.x - 10, pp.y - 10, 40, 40))
            for eee in self.en_el:
                if eee.is_out_of_bounds(self.setting.n_size, eee.los1):
                    self.reset(eee)
                    eee.hhh = 0

            p_list = self.grid.update_active_points()
            for pol in self.grid.connections:
                if not pol.broken:
                    start_pos = (pol.p1.x+10, pol.p1.y+10)
                    end_pos = (pol.p2.x+10, pol.p2.y+10)
                    pg.draw.line(self.screen, self.setting.green, start_pos=start_pos, end_pos=end_pos)

            for i in range(len(self.grid.points)):
                self.grid.points[i] = [p for p in self.grid.points[i] if p in p_list]

            pg.display.flip()
            self.clock.tick(50)
            li = []
            for eee in self.en_el:
                eee.sss += 10
                li.append([eee.x - 10, eee.y - 10])
            lista2.append(li)
            lista1.append(p_list)
            if mimi == 100000:
                break
            mimi = mimi+1
        dt = time.time()
        print(dt-ts)
        
        pg.quit()


