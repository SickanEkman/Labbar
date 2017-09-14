# from translator import Translator
from lexicon import Lexicon

def training():
    """takes the parallel corpus and sends it to lexicon"""
    # ../../smt/mini.txt
#    filename = input("What file should I train with?\n")
    my_lexicon = Lexicon()
    my_lexicon.hello_world()
    my_lexicon.readfile()
    my_lexicon.minimize()
    print(my_lexicon.l1_dict)

#    minimize(self, self.l1_dict)
#    big_dict = Lexicon.readfile(filename)
#    small_file = Lexicon.minimize(filename)

#def fix_translation():
#    """fixes the translation of user provided text"""
#    trans_list = []
#    org_sentence = input("What sentence would you like translated?\n")
#    org_words = org_sentence.split(" ")
#    org_words = Translator()
#    #should 1: ask for text to be translated
#    #should 2: use method in translator.py?

#def show_translation():
#    """print output to user"""

if __name__ == "__main__":  # this is just good practice. It doesn't mean anything?
    #program starts with user giving filename as argument
    training()



#somewhere in this mainfile I shuld split the list of files and send them one at the time to translator
''' for item in filenames:'''
