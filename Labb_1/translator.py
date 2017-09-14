class Translator(object):
    def __init__(self):
        pass

    def translate(self):
    """takes a sentence, returns the translation"""
        or_list = or_sentence.split(" ")
        for word in or_list:
            trans_word = lookup(word)
            trans_list.append(trans_word)
        trans_sentence = " ".join(trans_list)

#eller:?

    for word in org_words:
        trans_word = Lexicon.lexicon(org_word)
        trans_list.append(trans_word)
    trans_sentence = " ".join(trans_list)