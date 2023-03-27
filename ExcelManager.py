import openpyxl
import time


class ExcelManager:
    class Card:
        def __init__(self, values):
            self.level = values[0]
            self.A = values[1]
            self.B = values[2]
            self.extra = values[3]
            self.extraC = values[4]
            self.lastRevision = values[5]
            self.saveLine = values[6]

        def update(self, b_was_right):
            self.lastRevision = time.time()
            if b_was_right:
                self.level = self.level + 1
            else:
                if self.level > 1:
                    self.level = self.level + 1

        def get_values_to_save(self):
            values = [self.level, self.A, self.B, self.extra, self.extraC, self.lastRevision]
            return values

    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.load_workbook(filename)
        self.sheet = self.workbook.active
        self.currentLine = 1

    def get_row_data(self, row_num):
        row_data = []
        for cell in self.sheet[row_num][:5]:
            row_data.append(cell.value)
        return row_data

    def get_data(self):
        data = []
        b_is_going = True
        line = self.currentLine
        while b_is_going:

            value = self.sheet.cell(line, 1).value
            if value:
                print(value)
                data.append(self.get_row_data(line))
            else:
                print("hmm")
                print(line)
                print(value)
                b_is_going = False

            if len(data) > 10:
                print("joa nh")
                b_is_going = False
            line += 1
        self.currentLine = line
        return data

    def fill_row(self, card):

        for i, value in enumerate(card.get_values_to_save(), start=1):
            cell = self.sheet.cell(row=card.saveLine, column=i)
            cell.value = value

        self.workbook.save(self.filename)
