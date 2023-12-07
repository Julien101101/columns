# project5.py
# 
# commands being R < and >
# visual cue when fallers land and match
# create a tick instance (once per second)



import pygame
import jewel_columns


jewel_colors = [
    (244, 196, 48), 
    (0, 128, 128), 
    (217, 56, 30), 
    (161, 102, 47), 
    (255,182,193),
    (255, 255, 0), 
    (196, 192, 226)]


ROWS = 16
COLUMNS = 6





def main():
    pygame.init()

    surface = pygame.display.set_mode(500, 1200)

    running = True

    pygame.display.set_caption("Python Columns")
    clock = pygame.time.Clock()


    while running:
        clock.tick(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        surface.fill(pygame.Color(232, 111, 30))

        pygame.display.flip()

    columns_game = jewel_columns.ColumnsGrid(COLUMNS, ROWS)

    while True:
            # create an empty board
        board = []
        columns_game.initialize_empty_board_with_zeros(board)



        if jewel_columns.is_game_over():
            break

        parse_this = input()

        if parse_this == 'Q':
            break

        command = parse_this[0]

        if command == 'F':
            col = int(parse_this[2])

            # create a faller object
            
            # game_model.Jewel = parse_this[4]
            # game_model.Jewel = parse_this[6]
            # game_model.Jewel = parse_this[8]
        
        else:
            pass

        jewel_columns.handle_faller()
        

    print("GAME OVER")
    pygame.quit()


if __name__ == '__main__':
    main()