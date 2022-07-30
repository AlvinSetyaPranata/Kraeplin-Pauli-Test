from openpyxl import Workbook



class Writer:
    def __init__(self, filename):
        self._document = Workbook()
        self._sheet = self._document.active
        self.filename = filename


    @property
    def add_extension(self):
        return "".join((self.filename, ".", "xlsx"))


    def write(self, *cell_data):
        # :cell_data should be a list that contain [ row, column, value]
        # if :cell_data are empty then it will be recognize as whitespace

        for cell in cell_data:

            cell = "".join((cell[0], cell[1]))
            self._sheet[cell] = cell[-1]

        self._document.save(self.add_extension)
        
