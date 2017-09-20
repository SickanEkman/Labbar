class Translator(object):
    def __init__(self, lexicon, english):
        self.lexicon = lexicon
        self.text = self.modify_input(english)

    def modify_input(self, english):
        if ".txt" in english:
            with open(english, "r") as p_file:
                lines = p_file.readlines()
                lines = [i.strip("\n") for i in lines]
                text = " ".join(lines)
        else:
            text = english
        return text

    def translate(self):
        """takes a sentence, returns the translation"""
#        print(self.text) todo: delete later
        l1_list = self.text.split(' ')
        trans_list = []
        for word in l1_list:
            trans_word = self.lexicon.lookup(word)
            trans_list.append(trans_word)
        translation = " ".join(trans_list)
        return translation
