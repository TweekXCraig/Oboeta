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