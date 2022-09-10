import pygame
import numpy
import math

class Player:
    def __init__(self):
        self.pos = numpy.array([0, 0], dtype=float)
        self.angle = math.pi / 4
        self.height = 270
        self.pitch = 40
        self.angle_vel = 0.01
        self.vel = 3

    def update(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)

        press_key = pygame.key.get_pressed()

        if press_key[pygame.K_UP]:
            self.pitch += self.vel
        if press_key[pygame.K_DOWN]:
            self.pitch -= self.vel

        if press_key[pygame.K_LEFT]:
            self.angle -= self.angle_vel
        if press_key[pygame.K_RIGHT]:
            self.angle += self.angle_vel

        
        if press_key[pygame.K_q]:
            self.height += self.vel
        if press_key[pygame.K_e]:
            self.pitch -= self.vel

        if press_key[pygame.K_w]:
            self.pos[0] += self.vel * cos_a
            self.pos[1] += self.vel * sin_a
        if press_key[pygame.K_s]:
            self.pos[0] -= self.vel * cos_a
            self.pos[1] -= self.vel * sin_a
        if press_key[pygame.K_a]:
            self.pos[0] += self.vel * sin_a
            self.pos[1] -= self.vel * cos_a
        if press_key[pygame.K_d]:
            self.pos[0] -= self.vel * sin_a
            self.pos[1] += self.vel * cos_a
            