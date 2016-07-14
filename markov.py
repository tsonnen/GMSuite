''' 7/13/2106

    Generates a name based on a list of strings
    using a MArkov chain algorithm
'''

import random


class markovname:
    def __init__(self, nameList, order = 3):
        self.nameList = nameList
        self.table = dict()
        self.order = order

        for i in self.nameList:
            self.load(i.lower())

    def load(self, s):
        for i in range(len(s) - self.order):
            try:
                self.table[s[i:i + self.order]]
            except KeyError:
                self.table[s[i:i + self.order]] = []
            self.table[s[i:i + self.order]] += s[i + self.order]

    def generate(self, start = None, max_length = 20):
        if start == None:
            s = random.choice(list(self.table.keys()))
        else:
            s = start
        try:
            while len(s) < max_length:
                s += random.choice(self.table[s[-self.order:]])
        except KeyError:
            pass
        return s.capitalize()
