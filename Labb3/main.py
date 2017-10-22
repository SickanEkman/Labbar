import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Authenticate import api


class TweetScraper(object):
    def __init__(self, userlist):
        self.userlist = userlist

    def search_users(self):
        """Takes a list of names as input. For each name a Twitter search is made.
        Saves 'Username' and 'User ID' for all matching accounts, into one json-file for each search term.
        Files are named 'Different[Full Name].json' """
        for name in self.userlist:
            dict_json = {}
            x = 0
            users = api.GetUsersSearch(term=name)
            for user in users:
                id_number = "ID=" + str(user.id)
                screen_name = "ScreenName=" + user.screen_name
                json_str = json.JSONEncoder().encode({"User": [id_number, screen_name]})
                dict_json[x] = json_str
                x += 1
            with open("Different" + name + ".json", "w") as outfile:
                json.dump(dict_json, outfile)
            outfile.close()

    def get_posts(self, userid, username):
        """Takes 'User ID' and 'UserName' as input when called by user. Searches Twitter for the user's last 200 posts
        and saves them to json-file named 'tweetsFrom[username].json' """
        dict_json = {}
        x = 0
        outfile_name = "tweetsFrom" + username + ".json"
        posts = api.GetUserTimeline(user_id=userid, count=200)
        text_list = [p.text for p in posts]
        for text in text_list:
            dict_json[x] = text
            x += 1
        with open(outfile_name, "w") as outfile:
            json.dump(dict_json, outfile)
        outfile.close()


class Account(object):
    """Creates an Account object. Opens the file with tweets, and returns a Pandas-array.
    Looks at the array with Tweets and searches for all mentions of opponents name. Stores the count as object
    attributes."""
    def __init__(self, name, filename, op_name_a, op_name_b):
        self.own_name = name
        self.file = filename
        self.op_full_name = op_name_a + " " + op_name_b
        self.op_first_name = op_name_a
        self.op_last_name = op_name_b
        self.pandas_DataFrame = self.map_tweets()
        self.op_full_name_count, self.op_first_name_count, self.op_last_name_count = self.count_words()

    def map_tweets(self):
        with open(self.file, "r") as fin:
            data = json.load(fin)
            pandas_list = pd.DataFrame.from_dict(data, orient="index")
            fin.close()
            return pandas_list

    def count_words(self):
        full_name_count = 0
        first_name_count = 0
        last_name_count = 0
        for item in self.pandas_DataFrame.get_values():
            for text in item:
                if self.op_full_name in text:
                    print(text)
                    full_name_count += 1
                elif self.op_first_name in text:
                    print(text)
                    first_name_count += 1
                elif self.op_last_name in text:
                    print(text)
                    last_name_count += 1
                else:
                    pass
        print("FULL NAME:", full_name_count, "\nFIRST NAME:", first_name_count, "\nLAST NAME:", last_name_count)
        return full_name_count, first_name_count, last_name_count


class Visualizer(object):
    def __init__(self, account_1, account_2):
        self.own_name_1 = account_1.own_name
        self.op_full_name_count_1 = account_1.op_full_name_count
        self.op_first_name_count_1 = account_1.op_first_name_count
        self.op_last_name_count_1 = account_1.op_last_name_count
        self.own_name_2 = account_2.own_name
        self.op_full_name_count_2 = account_2.op_full_name_count
        self.op_first_name_count_2 = account_2.op_first_name_count
        self.op_last_name_count_2 = account_2.op_last_name_count

    def show_plot(self):
        """Creates a bar plot showing two accounts. For account A it shows mentions of owner of account B,
        and vice versa."""
        label_1 = (self.own_name_1 + "'s account")
        label_2 = (self.own_name_2 + "'s account")
        clusters = 3
        counts_1 = (self.op_full_name_count_1, self.op_first_name_count_1, self.op_last_name_count_1)
        counts_2 = (self.op_full_name_count_2, self.op_first_name_count_2, self.op_last_name_count_2)
        fig, ax = plt.subplots()
        index = np.arange(clusters)
        bar_width = 0.2
        opacity = 0.5
        rects1 = plt.bar(index, counts_1, bar_width, alpha=opacity, color="b", label=label_1)
        rects2 = plt.bar(index + bar_width, counts_2, bar_width, alpha=opacity, color="g", label=label_2)
        #plt.xlabel("Name forms")
        plt.ylabel("Number of references")
        plt.title("Reference of opponents name")
        plt.xticks(index + bar_width, ("Opponent's Full Name", "Opponent's First Name only", "Opponent's Last name only"))
        plt.legend()
        plt.tight_layout()
        plt.show()

# main
my_scraper = TweetScraper(["Hillary Clinton", "Donald Trump"])
my_scraper.search_users()
my_scraper.get_posts(1339835893, "HillaryClinton")  # 455818121: Sara's Twitter ID
                                                    # 1339835893: Hillary Clinton
                                                    # 25073877: Idiot
my_scraper.get_posts(25073877, "realDonaldTrump")
account_Hillary = Account("Hillary Clinton", "tweetsFromHillaryClinton.json", "Donald", "Trump")
account_Donald = Account("Donald Trump", "tweetsFromrealDonaldTrump.json", "Hillary", "Clinton")
my_visualiser = Visualizer(account_Hillary, account_Donald)
my_visualiser.show_plot()
