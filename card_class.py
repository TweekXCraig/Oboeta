import time


class Card:
    def __init__(self, values):

        self.A = values[0]
        self.Addon = values[1]
        self.B = values[2]
        self.extra = values[3]
        self.extraC = values[4]
        self.level = values[5]
        self.lastRevision = values[6]
        self.saveLine = values[7]
        print("A:", self.A)

    def update(self, b_was_right):
        self.lastRevision = time.time()
        if b_was_right:
            self.level = self.level + 1
        else:
            if self.level > 1:
                self.level = self.level + 1

    def get_to_test(self):
        test = self.A + " (" + self.Addon + ")"
        return test

    def get_values_to_save(self):
        values = [self.A, self.Addon, self.B, self.extra, self.extraC, self.level, self.lastRevision]
        return values

    def get_time_by_level(self):
        if self.level == 1:
            return 0
        elif self.level == 2:
            return 120
        elif self.level == 3:
            return 600
        elif self.level == 4:
            return 6000
        elif self.level == 5:
            return 46800
        elif self.level == 6:
            return 237600
        elif self.level == 7:
            return 669600
        elif self.level == 8:
            return 1101600
        elif self.level == 9:
            return 2138400
        elif self.level == 10:
            return 5000000
        elif self.level == 11:
            return 10000000
        elif self.level == 12:
            return 9999999999
        else:
            print("level data not int between 0 and 12. fix!?")
            print(self.level)
            return 91919191919191

    def b_is_due(self):
        due_date = self.lastRevision + self.get_time_by_level()
        if due_date <= time.time():
            return True
        elif due_date >= time.time():
            return False
        else:
            print("card_class -> b_is_due() calculation did not work :)")
            return None
