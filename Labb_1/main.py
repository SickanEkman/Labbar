from translator import Translator
from lexicon import Lexicon

def training():
    """takes the parallel corpus and sends it to lexicon"""
    my_lexicon = Lexicon() #creates the Lexicon object "my_lexicon"
    my_lexicon.hello_world() #test function todo: delete later!
    my_lexicon.readfile() #creates large lexicon from parallel file
    my_lexicon.minimize() #picks most frequent word as value
    print("These are the things: ", my_lexicon.__dict__, my_lexicon.l1_dict)
    return my_lexicon

def fix_translation(lexicon, text):
    """fixes the translation of user provided text"""
    my_translation = Translator(lexicon, text) #creates the Translator object "my_translator"
    translation = my_translation.translate(text)
    return translation

if __name__ == "__main__":  # this is just good practice. It doesn't mean anything?
    #program starts with user giving filename as argument
    lexicon = training()
    text = input("What text would you like translated?\n")
    translation = fix_translation(lexicon, text)
    print(translation)
