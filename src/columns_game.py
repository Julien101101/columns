# columns_game.py

import pygame
import jewel_columns
import math
from settings import *


class ColumnsGame:
    def __init__(self, app):
        self.app = app

    def draw_grid(self):
        for x in range(FIELD_W):
            for y in range(FIELD_H):
                pg.draw.rect(self.app.screen, 'white',
                             (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)
    def update(self):
        pass

    def draw(self):
        self.draw_grid()
        
#         self._running = True
#         self._state = jewel_columns.ColumnsState(columns, rows)

#     def run(self):
#         pygame.init()
#         self._resize_surface((500, 950))
#         clock = pygame.time.Clock()

#         while self._running:
#             clock.tick(FPS)
#             self._handle_events()
#             self._redraw()

#         pygame.quit()

#     def _handle_events(self):
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self._end_game()
#             elif event.type == pygame.VIDEORESIZE:
#                 self._resize_surface(event.size)
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT:
#                     self._state.move_faller_left()
#                 elif event.key == pygame.K_RIGHT:
#                     self._state.move_faller_right()
#                 if event.key == pygame.K_DOWN:
#                     self._state.move_faller_down()
#                 elif event.key == pygame.K_r:
#                     self._state.rotate_faller()

#     def _redraw(self):
#         surface = pygame.display.get_surface()
#         surface.fill(pygame.Color(FIELD_COLOR))
#         self._draw_grid()
#         self._draw_jewels()
#         pygame.display.flip()

    
#     def _draw_grid(self):
#         surface = pygame.display.get_surface()

#         for x in range(COLUMNS):
#             for y in range(ROWS):
#                 pygame.draw.rect(surface, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

#     def _draw_jewel(self, jewel, x, y):
#         surface = pygame.display.get_surface()
#         jewel_size = 40  # Adjust the size of the jewel as needed

#         # Calculate the screen coordinates for the jewel
#         screen_x = x * TILE_SIZE
#         screen_y = y * TILE_SIZE

#         # Draw a rectangle representing the jewel
#         pygame.draw.rect(surface, jewel.color, (screen_x, screen_y, jewel_size, jewel_size))

#     def _draw_jewels(self):
#         for jewel, (x, y) in self._state.all_jewels():
#             self._draw_jewel(jewel, x, y)

#     def _end_game(self):
#         self._running = False

#     def _resize_surface(self, size):
#         pygame.display.set_mode(size, pygame.RESIZABLE)
#         self._state = jewel_columns.ColumnsGrid(COLUMNS, ROWS)  # Create a new ColumnsGrid instance after resizing
#         self._state.initialize_empty_board()  # Reset the board when resizing
#         self._state.create_faller()  # Create a new faller after resizing

#     def _move_faller(self):
#         self._state.move_faller_left()
#         self._state.move_faller_right()
#         self._state.move_faller_down()


# if __name__ == "__main__":
#     ColumnsGame(columns=6, rows=16).run()
