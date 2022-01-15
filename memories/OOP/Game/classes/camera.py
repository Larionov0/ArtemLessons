from tools.math_ops import *


class Camera:
    def __init__(self, hero, width, height):
        self.hero = hero
        self.width = width
        self.height = height
        self.mouse_coords = [0, 0]
        self.k = 0.3

    def get_center_coords(self):
        hero_coords = [self.hero.x, self.hero.y]
        vector = [self.mouse_coords[0] - hero_coords[0], self.mouse_coords[1] - hero_coords[1]]
        small_vector = [vector[0] * self.k, vector[1] * self.k]
        return [hero_coords[0] + small_vector[0], hero_coords[1] + small_vector[1]]

    def get_left_up_coords(self):
        center = self.get_center_coords()
        return [center[0] - self.width // 2, center[1] - self.height // 2]

    def calc_coords(self, global_coords):
        coords = self.get_left_up_coords()
        return [global_coords[0] - coords[0], global_coords[1] - coords[1]]

    def local_to_global(self, local_coords):
        coords = self.get_left_up_coords()
        return [coords[0] + local_coords[0], coords[1] + local_coords[1]]

    def set_mouse_coords(self, coords):
        self.mouse_coords = coords
