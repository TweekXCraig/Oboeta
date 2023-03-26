import openpyxl


class ExcelManager:
    def __init__(self, filename):
        self.filename = filename
        self.workbook = openpyxl.load_workbook(filename)
        self.sheet = self.workbook.active

    def get_row_data(self, row_num):
        row_data = []
        for cell in self.sheet[row_num][:5]:
            row_data.append(cell.value)
        return row_data

    def get_data(self):
        data = []
        b_is_going = True
        line = 1
        while b_is_going:

            value = self.sheet.cell(line, 1 ).value
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
        return data

    def fill_row(self, row_num, values):
        for i, value in enumerate(values, start=1):
            cell = self.sheet.cell(row=row_num, column=i)
            cell.value = value

        self.workbook.save(self.filename)
