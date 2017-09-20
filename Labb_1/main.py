import sys
from translator import Translator
from lexicon import Lexicon


def training():
    """takes the parallel corpus and sends it to lexicon"""
    filename = sys.argv[1]  # todo: look at "sys.argv" in the doc
    my_lexicon = Lexicon(filename)  # creates the Lexicon object "my_lexicon"
    my_lexicon.readfile()  # creates large lexicon from parallel file
    my_lexicon.minimize()  # picks most frequent word as value
    return my_lexicon

if __name__ == "__main__":  # this is just good practice. It doesn't mean anything?
    lexicon = training()
    text = input("What text would you like translated?\n")
    my_translation = Translator(lexicon, text)  # creates the Translator object "my_translator"
    translation = my_translation.translate()
    print(translation)

# filename example "../../smt/en-es-2006-01.txt"