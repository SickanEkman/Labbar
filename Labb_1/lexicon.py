from itertools import islice
from collections import Counter


class Lexicon(object):
    def __init__(self):
        self.filename = "../../smt/mini.txt"
        self.l1_list = []
        self.l1_dict = {}
        self.l2_list = []
        self.mapping_list = []

    def hello_world(self):
        #todo: delete this funtion later
        print(self.l1_list,
        self.l1_dict,
        self.l2_list,
        self.mapping_list,
        self.filename
        )

    def readfile(self):
        """opens file and reads the relevant parts"""
        with open(self.filename, "r") as p_file:
            try:
                while True:  # tells program to continue til end of file
                    lines = list(islice(p_file, 5))  # creates a list with 5 lines
                    self.l1_list = lines[0].split(" ")  # creates list with English words
                    self.l2_list = lines[1].split(" ")  # creates list with Foreign words
                    self.mapping_list = lines[2].split(" ")  # creates list with mapping numbers
                    if "\n" in self.mapping_list[-1]:  # todo: remove the following str.strips and fix it from start
                        self.mapping_list[-1] = self.mapping_list[-1].strip("\n")
                    if "\n" in self.l1_list[-1]:
                        self.l1_list[-1] = self.l1_list[-1].strip("\n")
                    if "\n" in self.l2_list[-1]:
                        self.l2_list[-1] = self.l2_list[-1].strip("\n")
                    self.mapping_list = ["???" if i == "-1" else i for i in self.mapping_list]
                    print(self.mapping_list)  # todo: delete this line later!
                    # lines[3] + [4] do nothing
                    self.l1_dict = map(self.l1_list, self.l2_list, self.mapping_list)  # gets dict from function "map"
            except(IndexError):  # exception raised when whole parallel file is read
                print(self.l1_dict)  # todo: delete this line later!
                return self.l1_dict  # saves the dictionary
        p_file.close()  # uneccessary since "with file as..." is used, but good practice to have in function

    def map(self, l1_list, l2_list, mapping_list):
        """connects the l1 word to the l2 word"""
        x = 0
        while x < len(self.l1_list):
            z = self.l1_list[x].lower()  # point to English word with index x in list with English words
            try:
                y = int(self.mapping_list[x])  # creates an int from index x in list with mapping numbers
                value = self.l2_list[y].lower()
            except(ValueError):
                value = self.mapping_list[x]
            if z not in self.l1_dict:  # if the dictionary doesn't contain the English word
                self.l1_dict[z] = [value]  # puts English word as key, with list containing foreign word as value
            else:  # if English word is already in dictionary
                self.l1_dict[z].append(value)  # adds mapped foreign word as new list item in dictionary value
            x += 1
        return self.l1_dict

    def minimize(self):
        """counts most frequent translation and deletes the rest"""
        for k, v in self.l1_dict.items():
            count = Counter(v)
            frequency_list = [(k, count[k]) for k in sorted(count, key=count.get, reverse=True)]
            if frequency_list[0][0] == "???" and len(frequency_list) > 1:
                # print(frequency_list[1][0])  # todo: prints just to see that everything works - delete this line later!
                self.l1_dict[k] = frequency_list[1][0]
            else:
                # print(frequency_list[0][0]) # todo: prints just to see that everything works - delete this line later!
                self.l1_dict[k] = frequency_list[0][0]
        return self.l1_dict

    def lookup(self, word):
        """takes a word as argument and returns the translation"""
        word = word.lower()
        if word in l1_dict:
            return l1_dict.get(word)
        else:
            return "???"

