class Translator(object):
    def __init__(self, lexicon, text):
        self.lexicon = lexicon
        self.text = text

    def translate(self, text):
        """takes a sentence, returns the translation"""
        l1_list = text.split(' ')
        trans_list = []
        for word in l1_list:
            trans_word = self.lexicon.lookup(word)
            trans_list.append(trans_word)
        translation = " ".join(trans_list)
        return translation
