from itertools import islice
from collections import Counter

l1_list = []
l1_dict = {}
l2_list = []
mapping_list = []

def readfile(filename):
    """opens file and reads the relevant parts"""
    with open(filename, "r") as p_file:
        try:
            while True:  # tells program to continue til end of file
                lines = list(islice(p_file, 5))  # creates a list with 5 lines
                l1_list = lines[0].split(" ")  # creates list with English words
                l2_list = lines[1].split(" ")  # creates list with Foreign words
                mapping_list = lines[2].split(" ")  # creates list with mapping numbers
                mapping_list[-1] = mapping_list[-1].strip("\n")
                if "\n" in l1_list[-1]:
                    l1_list[-1] = l1_list[-1].strip("\n")
                if "\n" in l2_list[-1]:
                    l2_list[-1] = l2_list[-1].strip("\n")
                mapping_list = ["???" if i == "-1" else i for i in mapping_list]
                # lines[3] + [4] do nothing
                l1_dict = map(l1_list, l2_list, mapping_list)  # calls function "map", gets dictionary
        except(IndexError):  # exception raised when whole parallel file is read
            return l1_dict  # saves the dictionary
    p_file.close()  # uneccesary since "with file as..." is used, but good practice to have in function


def map(l1_list, l2_list, mapping_list):
    """connects the l1 word to the l2 word"""
    x = 0
    while x < len(l1_list):
        z = l1_list[x].lower()  # point to English word with index x in list with English words
        try:
            y = int(mapping_list[x])  # creates an int from index x in list with mapping numbers
            value = l2_list[y].lower()
        except(ValueError):
            value = mapping_list[x]
        if z not in l1_dict:  # if the dictionary doesn't contain the English word
            l1_dict[z] = [value]  # puts English word as key, with list containing foreign word as value
        else:  # if English word is already in dictionary
            l1_dict[z].append(value)  # adds mapped foreign word as new list item in dictionary value
        x += 1
    return l1_dict

def minimize(l1_dict):
    """counts most frequent translation and deletes the rest"""
    for k,v in l1_dict.items():
        count = Counter(v)
        frequency_list = [(k, count[k]) for k in sorted(count, key=count.get, reverse=True)]
        if frequency_list[0][0] == "???" and len(frequency_list) > 1:
            l1_dict[k] = frequency_list[1][0]
        else:
            l1_dict[k] = frequency_list[0][0]
    return(l1_dict)

def lookup(word):
    """takes a word as argument and returns the translation"""
    word = word.lower()
    if word in l1_dict:
        return l1_dict.get(word)
    else:
        return "???"

trans_list = []
l1_dict = readfile("../../smt/mini.txt")
l1_dict = minimize(l1_dict)
or_sentence = input("Hi there user! What sentence would you like translated?\n")
or_list = or_sentence.split(" ")
for word in or_list:
    trans_word = lookup(word)
    trans_list.append(trans_word)
trans_sentence = " ".join(trans_list)
print(trans_sentence)