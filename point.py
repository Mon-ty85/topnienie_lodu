# point.py
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.x0 = x
        self.y = y
        self.y0 = y
        self.move = False
        self.osc_force_y = 0  # Zmieniono na 0, jak w oryginalnym kodzie
        self.osc_force_x = 0  # Zmieniono na 0, jak w oryginalnym kodzie
        self.line_num = 0

    def collide(self, en_x, en_y, en_el, settings):
        if abs(self.x0 - en_x) < 40 and abs(self.y0 - en_y) < 40:
            if not self.move:
                self.x0 = self.x
                self.y0 = self.y
                self.move = True

            osc_x = 0
            osc_y = 0

            """if settings.option == 1:
                """
            draw = np.random.choice([0, 1])
            if self.line_num == 2:
                    if draw == 0:
                        osc_x += 20
                    elif draw == 1:
                        osc_y += 20
            elif self.line_num == 1:
                    if draw == 0:
                        osc_x += 45
                    elif draw == 1:
                        osc_y += 45
            elif self.line_num == 3:
                    if draw == 0:
                        osc_x += 5
                    elif draw == 1:
                        osc_y += 5
            """else:
                if en_el.right or en_el.left:
                    if self.line_num == 2:
                        osc_x += 20
                    elif self.line_num == 1:
                        osc_x += 45
                    elif self.line_num == 3:
                        osc_x += 5
                elif en_el.up or en_el.down:
                    if self.line_num == 2:
                        osc_y += 20
                    elif self.line_num == 1:
                        osc_y += 45
                    elif self.line_num == 3:
                        osc_y += 5"""

            self.osc_force_x += osc_x
            self.osc_force_y += osc_y

            return True, osc_x, osc_y
        return False

    def update_position(self, t):
        def osscillate_x(t1, hh1):
            return hh1 / 2 * np.sin(10 * t1 + hh1)

        def osscillate_y(t2, hh2):
            return hh2 / 2 * np.sin(10 * t2 + hh2)

        if self.move:
            self.x = self.x0 + osscillate_x(t, self.osc_force_x)
            self.y = self.y0 + osscillate_y(t, self.osc_force_y)