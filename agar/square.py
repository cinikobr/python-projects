class Square:
    id: int
    radius: int
    sx: int
    sy: int

    def __init__(self, s_id: int, radius: int, sx: int, sy: int):
        self.id = s_id
        self.radius = radius
        self.sx = sx
        self.sy = sy

    def get_id(self):
        return self.id

    def get_radius(self):
        return self.radius

    def get_sx(self):
        return self.sx

    def get_sy(self):
        return self.sy

    def set_radius(self, radius):
        self.radius = radius

    def set_sx(self, sx):
        self.sx = sx

    def set_sy(self, sy):
        self.sy = sy


