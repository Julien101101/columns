import random

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

    @property
    def faller(self) -> list[tuple[int, int, int]]:
        return self._faller


    @staticmethod
    def random_generator(color_list: list[tuple[str, tuple[int, int, int]]]) -> None:
        number_of_jewels = len(color_list)
        for i in range(0,3):
            if number_of_jewels > 0:
                value = random.randint(0, number_of_jewels - 1)
                selected_color = color_list[value]
                print(f"Randomly selected color: {selected_color}")
            else:
                print("No colors available.")


if __name__ == "__main__":
    mine_shaft = PopulateMineShaft()
    for i in mine_shaft.colors:
        if i == mine_shaft.colors[-1]:
            print(i)
        else:
            print(i, end = '')

    mine = CreateFaller(mine_shaft.colors)


    # so now that we have this working let us figure out a way to create a faller of three of these. . So we will have 3 
