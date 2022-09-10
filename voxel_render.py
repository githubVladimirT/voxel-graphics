from numba import njit
import pygame
import numpy
import math

height_map_img = pygame.image.load("img/height_map.jpg")
height_map = pygame.surfarray.array3d(height_map_img)

color_map_img = pygame.image.load("img/color_map.jpg")
color_map = pygame.surfarray.array3d(color_map_img)

map_height = len(height_map[0])
map_width = len(height_map)

@njit(fastmath=True)
def ray_casting(screen_array, player_pos, player_angle, player_height, player_pitch,
                screen_width, screen_height, delta_angle, ray_distance, h_fov, scale_height):

    screen_array[:] = numpy.array([0, 0, 0])
    y_buffer = numpy.full(screen_width, screen_height)
    ray_angle = player_angle - h_fov

    for num_ray in range(screen_width):
        first_contact = False
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        for depth in range(1, ray_distance):
            x = int(player_pos[0] + depth * cos_a)
            
            if 0 < x < map_width:
                y = int(player_pos[1] + depth * sin_a)

                if 0 < y < map_height:
                    depth *= math.cos(player_angle - ray_angle)
                    height_on_screen = int(
                                            (player_height - height_map[x, y][0]) / depth
                                            * scale_height + player_pitch)
                    
                    if not first_contact:
                        y_buffer[num_ray] = min(height_on_screen, screen_height)
                        first_contact = True

                    if height_on_screen < 0:
                        height_on_screen = 0

                    if height_on_screen < y_buffer[num_ray]:
                        for screen_y in range(height_on_screen, y_buffer[num_ray]):
                            screen_array[num_ray, screen_y] = color_map[x, y]
                        
                        y_buffer[num_ray] = height_on_screen
        
        ray_angle += delta_angle

    return screen_array

class VoxelRender:
    def __init__(self, app):
        self.app = app
        self.player = app.player
        self.fov = math.pi / 3
        self.h_fov = self.fov / 2
        self.num_arrays = app.width
        self.delta_angle = self.fov / self.num_arrays
        self.ray_distance = 2000
        self.scale_height = 620
        self.screen_array = numpy.full((app.width, app.height, 3), (0, 0, 0))

    def update(self):
        self.screen_array = ray_casting(self.screen_array, self.player.pos, self.player.angle,
                                        self.player.height, self.player.pitch, self.app.width,
                                        self.app.height, self.delta_angle, self.ray_distance,
                                        self.h_fov, self.scale_height)
        # Color random: self.screen_array =  numpy.random.randint(0, 255, size=self.screen_array.shape)

    def draw(self):
        self.app.screen.blit(pygame.surfarray.make_surface(self.screen_array), (0, 0))
