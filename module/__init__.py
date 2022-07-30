from writer import Writer
from random import randint

# Dev


# Release



# --------- Program Starts ------------- #



class Maker(Writer):
    def __init__(self, x_size, y_size, fname="exam"):
        self.x_size = x_size
        self.y_size = y_size

        self._current_row = 0
        self._current_col = 65
        self.fname = fname

        super().__init__(fname)


    def make(self):
        data = []

        for _ in range(self.x_size):
            if self._current_row == self.y_size:
                break

            data.append([self._current_row, chr(self._current_col), randint(1, 9)])


        self.write(data)

