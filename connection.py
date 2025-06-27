# connection.py
from settings import Settings

class Connection:
    def __init__(self, p1, p2):
        self.sett = Settings(4)
        self.p1 = p1
        self.p2 = p2
        self.broken = False

    def check_broken(self):
        if not self.broken:
            if abs(self.p1.x - self.p2.x) > 60 or abs(self.p1.y - self.p2.y) > 60:
                self.broken = True
                self.p1.line_num -= 1
                self.p2.line_num -= 1
        return not self.broken