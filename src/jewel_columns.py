from settings import *

class Block(pg.sprite.Sprite):
    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, pos):
       
       # Call the parent class (Sprite) constructor
       pg.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pg.Surface([width, height])
       self.image.fill(color)
       self.rect.topleft = pos[0] * TILE_SIZE, pos[1] * TILE_SIZE

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()


class PopulateMineShaft:
    def __init__(self):
        self.colors = PopulateMineShaft.generate_colors(self)

    def generate_colors(self) -> list[tuple[str, tuple[int, int, int]]]:
        possible_colors = ['S', 'T', 'V', 'W', 'X', 'Y', 'Z']
        color_tuples = []

        for color_key in possible_colors:
            # Generate a random RGB tuple for each color
            rgb_tuple = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
            color_tuples.append((color_key, rgb_tuple))

        # Update the instance attribute with the generated colors
        self.colors = color_tuples
        return color_tuples



class CreateFaller:
    def __init__(self, color_list: list[tuple[str, tuple[int, int, int]]]):
        self._faller = CreateFaller.random_generator(color_list)
        self._pos = (3, 0)


    @property
    def faller(self) -> list[tuple[int, int, int]]:
        return self._faller


    @classmethod
    def random_generator(cls, color_list: list[tuple[str, tuple[int, int, int]]]) -> list[tuple[int, int, int]]:
        faller = []
        for i in range(0, 3):
            value = random.randint(0, len(color_list) - 1)
            selected_color = color_list[value][1]
            faller.append(selected_color)
        return faller

    def rotate_faller(self):
        # Switch the positions of elements
        self._faller = [self._faller[1], self._faller[2], self._faller[0]]

    @classmethod
    def move_faller(cls, pos):
        pass



if __name__ == "__main__":
    mine_shaft = PopulateMineShaft()

    print(mine_shaft.colors)

    sailor = CreateFaller(mine_shaft.colors)

    while True:
        print(sailor.faller)   
        sailor.rotate_faller()
    

    # in order to be able to rotate the faller we should store the object in a list

