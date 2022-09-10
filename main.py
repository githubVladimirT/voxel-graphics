import os
os.system("clear")
print("\t\t\tInfo:")

import pygame
from player import Player
from voxel_render import VoxelRender

class App:
    def __init__(self):
        self.res = self.width, self.height = (800, 450)
        self.screen = pygame.display.set_mode(self.res, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.voxel_render = VoxelRender(self)

    def update(self):
        self.player.update()
        self.voxel_render.update()

    def draw(self):
        self.voxel_render.draw()
        pygame.display.flip()

    def run(self):
        while True:
            self.update()
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            
            self.clock.tick(60)
            pygame.display.set_caption(f"FPS: {int(self.clock.get_fps())}")

if __name__ == '__main__':
    try:
        app = App()
        app.run()
    except KeyboardInterrupt:
        print("\nExit")
    except SystemError:
        print("\nSystemError: CPUDispatcher")
