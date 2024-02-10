import pygame
import sys
import math
import numpy as np

from pygame.locals import *

# Definición de colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

# Definición de constantes para el cubo
CUBE_SIZE = 80
CUBIE_SIZE = 20
CUBIE_GAP = 2
MOVEMENT_SPEED = 5

class Cubie:
    def __init__(self, position, colors):
        self.position = position
        self.colors = colors

    def draw(self, surface, rotation_matrix):
        for i in range(6):
            face = self.get_face(i)
            rotated_face = self.rotate_face(face, rotation_matrix)
            face_int = [(int(point[0] * CUBE_SIZE + 400), int(point[1] * CUBE_SIZE + 300)) for point in rotated_face]
            pygame.draw.polygon(surface, self.colors[i], face_int)

    def get_face(self, index):
        x, y, z = self.position
        if index == 0:
            return [(x-0.5, y-0.5, z-0.5), (x+0.5, y-0.5, z-0.5), (x+0.5, y+0.5, z-0.5), (x-0.5, y+0.5, z-0.5)]
        elif index == 1:
            return [(x-0.5, y-0.5, z+0.5), (x+0.5, y-0.5, z+0.5), (x+0.5, y+0.5, z+0.5), (x-0.5, y+0.5, z+0.5)]
        elif index == 2:
            return [(x+0.5, y-0.5, z-0.5), (x+0.5, y-0.5, z+0.5), (x+0.5, y+0.5, z+0.5), (x+0.5, y+0.5, z-0.5)]
        elif index == 3:
            return [(x-0.5, y-0.5, z-0.5), (x-0.5, y-0.5, z+0.5), (x-0.5, y+0.5, z+0.5), (x-0.5, y+0.5, z-0.5)]
        elif index == 4:
            return [(x-0.5, y+0.5, z-0.5), (x+0.5, y+0.5, z-0.5), (x+0.5, y+0.5, z+0.5), (x-0.5, y+0.5, z+0.5)]
        elif index == 5:
            return [(x-0.5, y-0.5, z-0.5), (x+0.5, y-0.5, z-0.5), (x+0.5, y-0.5, z+0.5), (x-0.5, y-0.5, z+0.5)]

    def rotate_face(self, face, rotation_matrix):
        rotated_face = []
        for point in face:
            rotated_point = (
                rotation_matrix[0][0] * point[0] + rotation_matrix[0][1] * point[1] + rotation_matrix[0][2] * point[2],
                rotation_matrix[1][0] * point[0] + rotation_matrix[1][1] * point[1] + rotation_matrix[1][2] * point[2],
                rotation_matrix[2][0] * point[0] + rotation_matrix[2][1] * point[1] + rotation_matrix[2][2] * point[2]
            )
            rotated_face.append(rotated_point)
        return rotated_face

class RubiksCube:
    def __init__(self):
        self.cubies = []
        self.create_cubies()

    def create_cubies(self):
        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if (x == 0) + (y == 0) + (z == 0) == 2:
                        position = (x, y, z)
                        if x == -1:
                            colors = [RED, RED, RED, RED, BLACK, BLACK]
                        elif x == 1:
                            colors = [ORANGE, ORANGE, ORANGE, ORANGE, BLACK, BLACK]
                        elif y == -1:
                            colors = [GREEN, GREEN, GREEN, GREEN, BLACK, BLACK]
                        elif y == 1:
                            colors = [BLUE, BLUE, BLUE, BLUE, BLACK, BLACK]
                        elif z == -1:
                            colors = [WHITE, WHITE, WHITE, WHITE, BLACK, BLACK]
                        elif z == 1:
                            colors = [YELLOW, YELLOW, YELLOW, YELLOW, BLACK, BLACK]
                        self.cubies.append(Cubie(position, colors))

    def draw(self, surface, rotation_matrix):
        for cubie in self.cubies:
            cubie.draw(surface, rotation_matrix)

def rotate_around_x(angle):
    return [
        [1, 0, 0],
        [0, math.cos(angle), -math.sin(angle)],
        [0, math.sin(angle), math.cos(angle)]
    ]

def rotate_around_y(angle):
    return [
        [math.cos(angle), 0, math.sin(angle)],
        [0, 1, 0],
        [-math.sin(angle), 0, math.cos(angle)]
    ]

def rotate_around_z(angle):
    return [
        [math.cos(angle), -math.sin(angle), 0],
        [math.sin(angle), math.cos(angle), 0],
        [0, 0, 1]
    ]

def main():
    pygame.init()
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Rubik\'s Cube')
    clock = pygame.time.Clock()
    rubiks_cube = RubiksCube()
    angle_x = 0
    angle_y = 0
    angle_z = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            angle_y -= math.radians(MOVEMENT_SPEED)
        if keys[K_RIGHT]:
            angle_y += math.radians(MOVEMENT_SPEED)
        if keys[K_UP]:
            angle_x -= math.radians(MOVEMENT_SPEED)
        if keys[K_DOWN]:
            angle_x += math.radians(MOVEMENT_SPEED)

        screen.fill(WHITE)
        rotation_matrix = np.eye(3)
        rotation_matrix = np.dot(rotate_around_y(angle_y), rotation_matrix)
        rotation_matrix = np.dot(rotate_around_x(angle_x), rotation_matrix)

        rubiks_cube.draw(screen, rotation_matrix)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
