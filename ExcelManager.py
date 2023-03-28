import openpyxl
from card_class import Card
import time


class ExcelManager:

    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.load_workbook(filename)
        self.sheet = self.workbook.active
        self.currentLine = 1
        self.busLength = 10
        self.bus = []

    def get_row_data(self, row_num):
        row_data = []
        for cell in self.sheet[row_num][:6]:
            row_data.append(cell.value)
        if len(row_data) == 5:
            row_data.append(time.time())
        # checks of too little info is given, returns none if that's the case
        elif len(row_data) < 5:
            print("not enough cells used in line ", row_num)
            return None
        # checks if too much info is given, returns none if that's the case
        elif len(row_data) > 6:
            print("too many cells used in line ", row_num)
            return None
        row_data.append(row_num)
        print(len(row_data))
        return row_data

    @staticmethod
    def row_data_to_card(data):
        if len(data) == 7:
            card = Card(data)
            return card
        else:
            return None

    def get_data(self):
        data = []
        b_is_going = True
        line = self.currentLine
        while b_is_going:

            value = self.sheet.cell(line, 1).value
            if value:
                # print(value)
                data.append(self.get_row_data(line))
            else:
                print("ended at line:", line)
                print(value)
                b_is_going = False

            if len(data) > 10:
                b_is_going = False
            line += 1
        self.currentLine = line
        return data

    def fill_row(self, card):

        for i, value in enumerate(card.get_values_to_save(), start=1):
            cell = self.sheet.cell(row=card.saveLine, column=i)
            cell.value = value

        self.workbook.save(self.filename)
