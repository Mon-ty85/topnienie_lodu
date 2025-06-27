class Settings:
    def __init__(self, op):
        self.n_size = 20
        self.screen_width = 100+self.n_size*55
        self.screen_height = 100+self.n_size*55
        self.l_ele = 10
        self.black = (0, 1, 1)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.option = op