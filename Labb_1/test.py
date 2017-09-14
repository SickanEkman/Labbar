from itertools import islice
from collections import Counter

l1_list = []
l1_dict = {}
l2_list = []
mapping_list = []

def readfile():
    """opens file and reads words to dict"""
    with open("../../smt/mini.txt", "r") as p_file:
        print(p_file)
        try:
            while True:  # tells program to continue til end of file
                lines = list(islice(p_file, 5))  # creates a list with 5 lines
                lines = [s.strip("\n") for s in lines]
                l1_list = lines[0].split(" ")  # creates list with English words
                l2_list = lines[1].split(" ")  # creates list with Foreign words
                mapping_list = lines[2].split(" ")  # creates list with mapping numbers
                # mapping_list = ["???" if i == "-1" else i for i in mapping_list]
                # lines[3] + [4] do nothing
                l1_dict = mapping(l1_list, l2_list, mapping_list)  # gets dict from function "map"
        except IndexError:  # exception raised when whole parallel file is read
            return l1_dict  # saves the dictionary
    print("ending readfile, this is l1_dict: ", l1_dict)
    p_file.close()  # uneccessary since "with file as..." is used, but good practice to have in function

def mapping(l1_list, l2_list, mapping_list):
        """connects the l1 word to the l2 word"""
        x = 0
        while x < len(l1_list):  # loops through all items in list
            z = l1_list[x].lower()  # z = English word with index x in l1_list
            y = int(mapping_list[x])  # y = int from index x in mapping_list
            value = l2_list[y].lower() # value = foreign word
            if z not in l1_dict and y != -1:  # if the dictionary doesn't contain the English word
                l1_dict[z] = [value]  # puts English word as key, with list containing foreign word as value
            elif z in l1_dict and y != -1:  # if English word is already in dictionary
                l1_dict[z].append(value)  # adds mapped foreign word as new list item in dictionary value
            x += 1
        # print(l1_dict)
        return l1_dict

readfile()
print(l1_dict)