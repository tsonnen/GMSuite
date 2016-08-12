'''  8/11/2016

    Generates a name based on a list of strings
    using a Markov chain algorithm
'''

import random


class markovname:
    def __init__(self, nameList, order = 3):
        self.nameList = nameList
        self.table = dict()
        self.order = order

        for i in self.nameList:
            i = "\x02{0}\x03".format(i)
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
            s = "s"
            while(s[0] != "\x02"):
                s = random.choice(list(self.table.keys()))
        else:
            s = start
        try:
            nextVal = "nextVal"
            while len(s) < max_length:
                nextVal = random.choice(self.table[s[-self.order:]])
                print(self.table[s[-self.order:]])
                if(nextVal != "\x03"):
                    s += nextVal
                else:
                    break

                print(s)

            s = s.replace("\x02", "")
        except KeyError:
            pass
        return s.capitalize()
