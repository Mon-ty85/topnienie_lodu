import numpy as np

class Energy_el:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.up = False
        self.right = False
        self.left = False
        self.down = False
        self.sss = 0
        self.hhh = 0
        self.los1 = 0

    def update_position(self, ll):
        en_x = self.x
        en_y = self.y
        #los1 = np.random.randint(-10,10)
        if self.right:
            en_x -= self.sss
            en_y += self.sss*ll
        elif self.left:
            en_x += self.sss
            en_y += self.sss*ll
        if self.up:
            en_y += self.sss
            en_x += self.sss*ll
        elif self.down:
            en_y -= self.sss
            en_x += self.sss*ll
        return en_x, en_y

    def is_out_of_bounds(self, nn, ll):
        en_x, en_y = self.update_position(ll)
        return (self.right and en_x < -10) or \
               (self.up and en_y > 210+nn*50) or \
               (self.left and en_x > 210+nn*50) or \
               (self.down and en_y < -10)