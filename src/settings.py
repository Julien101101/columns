import pygame as pg
import random

vec = pg.math.Vector2

FPS = 1
FIELD_COLOR = (37, 150, 190)

TILE_SIZE = 50

FIELD_SIZE = FIELD_W, FIELD_H = 10, 20
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE

INIT_POS_OFFSET = vec(FIELD_SIZE) // 2

FALLING_ROCK = [(0, 0), (0, -1), (0, -2)] 