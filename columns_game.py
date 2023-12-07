# columns_game
#
#
# Jewels populate the columns
# Jewels can match with other jewels
# Jewels can fall down
# The falling of the jewels is the faller
# the faller can be controlled
# < , > to move left and right
# R to rotate




import pygame
import jewel_columns


class ColumnsGame:
    # i am afraid to make a mistake but i will full send
    # how can i init something and use it with what ive 
    # made in the game model...
    def __init__(self, board: list[list[int]]):
        self._running = True
        self._state = jewel_columns.ColumnsState()

        

    def run(self) -> None:
        pygame.init()

        self._resize_surface((500,1200))

        clock = pygame.time.Clock()

        while self._running:
            clock.tick(1)
            self._handle_events()
            self._redraw()

        pygame.quit()

    
    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._end_game()
                elif event.type == pygame.event.VIDFORESIZE:
                    self._resize_surface(event.size)
                elif event.type == pygame.event.LEFTKEY:
                    self._on_left_key(event.grid)
                elif event.type == pygame.event.RIGHTKEY:
                    self._on_right_key(event.grid)
            
            self._move_spots()

    
    def _redraw(self) -> None:
        surface = pygame.display.get_surface()

        surface.fill(pygame.Color(120, 0, 20))
        self._draw_jewels()

        pygame.display.flip()

    
    DEF
    
     
if __name__ == "__main__":
    ColumnsGame().run()