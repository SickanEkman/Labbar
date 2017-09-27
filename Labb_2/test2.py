from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression

class TagPredictor(object):
    def __init__(self, train_data, test_data):
        self.affix_list_train, self.pos_list_train = self.separate_tagged_list(train_data)
        self.dv = DictVectorizer()
        self.le = LabelEncoder()
        self.lr = LogisticRegression()
        self.x = self.dv.fit_transform(self.affix_list_train)
        self.y = self.le.fit_transform(self.pos_list_train)
        self.model = self.lr.fit(self.x, self.y)
        self.affix_list_test, self.pos_list_test = self.separate_tagged_list(test_data)

    def predict(self):
        error = 0
        #with open("result_file.txt", "w") as fout:
        #print("printing affix_list & pos_list: ", self.affix_list, self.pos_list)
        #print("printing affix & pos length: ", len(self.affix_list), "&", len(self.pos_list))
        #print("printing types x & y: ", type(self.x), type(self.y))
        #print("printing types dv, le & lr: ", type(self.dv), type(self.le), type(self.lr))
        z = self.lr.predict(self.dv.transform(self.affix_list_test))
        #z = self.dv.transform(self.affix_list)
        #print(type(z))
        #print(dir(z))
        #print(z.check_format)
        answer = self.le.inverse_transform(z)
        x = 0
        max_times = len(answer) - 1
        while x < max_times:
            if answer[x] != self.pos_list_train[x]:
                error += 1
            x += 1
        #print(answer)
        #fout.write(answer)
        print("I MADE IT TO PRINT!!!\n"
              "Error =", error, "\nPOS-list =", len(self.pos_list_train))

    def separate_tagged_list(self, tagged_list):
        #print(tagged_list)
        word_list = []
        pos_list = []
        for pair in tagged_list:
            word_list.append(pair[0])
            pos_list.append(pair[1])
        affix_list = self.create_affixes(word_list)
        #print("word_list: ", word_list, "\n",
        #      "affix_list: ", affix_list, "\n",
        #      "pos_list: ",  pos_list) #todo: remove later
        return affix_list, pos_list

    def create_affixes(self, word_list): #todo: create max len affixes == 5 chars.
        affix_list = []
        for word in word_list:
            affix_dictionary = {}
            counter_up = 1
            counter_down = len(word) -1
            while counter_up < (len(word) -1):
                if len(word[:counter_up]) < 6:
                    affix_dictionary[word[:counter_up]] = 1
                else:
                    pass
                counter_up += 1
            while counter_down >= 2:
                if len(word[counter_down:]) < 6:
                    affix_dictionary[word[counter_down:]] = 1
                else:
                    pass
                counter_down -= 1
            affix_list.append(affix_dictionary)
#        print(affix_list) todo: remove later
        return affix_list

def read_data(filename):
    tagged_list = []
    with open(filename, "r") as fin:
        lines = fin.readlines()
        for line in lines:
            line = line.split("\t")
            if len(line) > 1 and len(line[1]) > 3:
                tagged_set = (line[1], line[3])
                tagged_list.append(tagged_set)
        #print("TAGGED_LIST", tagged_list)
        return(tagged_list)

#main
training_file = input("What file do you want to train with?\n")
test_file = input("What file do you want to test your tagger with?\n")
train_tagged_list = read_data(training_file)
test_tagged_list = read_data(test_file)
my_predictor = TagPredictor(train_tagged_list, test_tagged_list)
my_predictor.predict()