import openpyxl
from card_class import Card
import time


def row_data_to_card(data):
    if len(data) == 8:
        card = Card(data)
        return card
    else:
        return None


class ExcelManager:

    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.load_workbook(filename)
        self.sheet = self.workbook.active
        self.currentLine = 1
        self.busLength = 10
        self.bus = []
        self.fill_bus()
        self.currentCard = self.get_current_card()

    def get_row_data(self, row_num):
        row_data = []
        for cell in self.sheet[row_num][:7]:
            row_data.append(cell.value)
        if row_data[0] is None:
            return 1
        elif len(row_data) == 6:
            row_data.append(time.time())
        # checks of too little info is given, returns none if that's the case
        elif len(row_data) < 6:
            print("not enough cells used in line ", row_num)
            return 1
        # checks if too much info is given, returns none if that's the case
        elif len(row_data) > 7:
            print("too many cells used in line ", row_num)
            return 1
        row_data.append(row_num)
        # print(row_data)
        # print(self.bus)
        return row_data

    def fill_bus(self):
        ToFill = self.busLength - len(self.bus)
        b_is_going = True
        while ToFill > 0 and b_is_going:
            if not self.get_row_data(self.currentLine) == 1:
                card = row_data_to_card(self.get_row_data(self.currentLine))
                if card.b_is_due():
                    self.bus.append(card)
                    ToFill -= 1
                self.currentLine += 1
            else:
                b_is_going = False
        print(len(self.bus))
        return

    def fill_row(self, card):

        for i, value in enumerate(card.get_values_to_save(), start=1):
            cell = self.sheet.cell(row=card.saveLine, column=i)
            cell.value = value

        self.workbook.save(self.filename)

    def save_bus(self):
        for card in self.bus:
            print(card.A)
            self.fill_row(card)
        return True

    def get_current_card(self):
        if len(self.bus) == 0:
            print("bus is empty")
            return None
        else:
            return self.bus[0]

    def check_input(self, input):
        self.currentCard.update_last_revision()
        if input == self.currentCard.B:
            self.currentCard.level_up()
            self.fill_row(self.currentCard)

            if len(self.bus) > 0:
                self.bus.pop(0)
                self.currentCard = self.get_current_card()
            return True
        else:
            self.currentCard.reset_level()
            return False
