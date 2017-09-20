from itertools import islice
from collections import Counter


class Lexicon(object):
    def __init__(self, filename):
        print("(Lexicon object created)")
        self.filename = filename
        self.l1_list = []
        self.l1_dict = {}
        self.l2_list = []
        self.mapping_list = []

    def readfile(self):
        """opens file and reads words to dict"""
        with open(self.filename, "r") as p_file:
            try:
                while True:  # tells program to continue til end of file
                    lines = list(islice(p_file, 5))  # creates a list with 5 lines
                    lines = [i.strip("\n") for i in lines]
                    self.l1_list = lines[0].split(" ")  # creates list with English words
                    self.l2_list = lines[1].split(" ")  # creates list with Foreign words
                    self.mapping_list = lines[2].split(" ")  # creates list with mapping numbers
                    # lines[3] + [4] do nothing
                    self.l1_dict = self.mapping()  # gets dict from function "map"
            except IndexError:  # exception raised when whole parallel file is read
                p_file.close()  # uneccessary since "with file as..." is used, but good practice to have in function
                return self.l1_dict  # saves the dictionary

    def mapping(self):
        """connects the l1 word to the l2 word"""
        counter = 0
        while counter < len(self.l1_list):  # runs through the whole l1_list
            english_word = self.l1_list[counter].lower()
            mapping_value = int(self.mapping_list[counter])
            foreign_word = self.l2_list[mapping_value].lower()
            if english_word not in self.l1_dict and mapping_value != -1:
                self.l1_dict[english_word] = [foreign_word]
            elif english_word in self.l1_dict and mapping_value != -1:
                self.l1_dict[english_word].append(foreign_word)
            counter += 1
        return self.l1_dict

    def minimize(self):
        """counts most frequent translation and deletes the rest"""
        for k, v in self.l1_dict.items():
            count = Counter(v)
            frequency_list = [(k, count[k]) for k in sorted(count, key=count.get, reverse=True)]
            self.l1_dict[k] = frequency_list[0][0]
        return self.l1_dict

    def lookup(self, word):
        """takes a word as argument and returns the translation"""
        word = word.lower()
        if word in self.l1_dict:
            return self.l1_dict.get(word)
        else:
            return "???"
