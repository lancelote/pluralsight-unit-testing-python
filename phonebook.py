# coding=utf-8

""""
Phonebook production code
"""


class Phonebook(object):

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        self.entries[name] = number

    def lookup(self, name):
        return self.entries[name]

    def get_names(self):
        return self.entries.keys()

    def is_consistent(self):
        numbers = list(self.entries.values())

        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if numbers[j].startswith(numbers[i]) or\
                   numbers[i].startswith(numbers[j]):
                    return False
        return True

