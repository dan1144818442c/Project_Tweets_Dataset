import pandas as pd
class Data_investigation:
    def __init__(self , df):
        self.df = df
        self.df_antisemitic = self.df[self.df['Biased'] ==  1]
        self.df_non_antisemitic = self.df[self.df['Biased'] ==  0]
        self.add_column_len_text()
        self.add_column_Number_of_words()


    def count_from_category(self  , name_category = 'Biased'):
        return self.df[name_category].value_counts().to_dict()

    def add_column_Number_of_words(self, column_name = 'Text'):
        self.df['Number_of_words']  =self.df[column_name].transform(lambda x : len(x.strip().split(" ")) )
        self.df_antisemitic = self.df[self.df['Biased'] == 1]
        self.df_non_antisemitic = self.df[self.df['Biased'] == 0]

    def add_column_len_text(self, column_name = 'Text'):
        self.df['len_text'] = self.df[column_name].transform(lambda x : len(x) )
        self.df_antisemitic = self.df[self.df['Biased'] == 1]
        self.df_non_antisemitic = self.df[self.df['Biased'] == 0]

    def evrage_words_tweest(self ):

        average_all = self.df['Number_of_words'].mean()
        average_df_antisemitic = self.df_antisemitic['Number_of_words'].mean()
        average_df_non_antisemitic = self.df_non_antisemitic['Number_of_words'].mean()

        dic_res = {"total"  : float(average_all) , "average_df_antisemitic" :float( average_df_antisemitic)  , "average_df_non_antisemitic"  : float( average_df_non_antisemitic)}
        return dic_res

    def longest_3_tweets(self , column_name = 'Text'):
        # longest_3_tweets_antisemitic_1 = self.df_antisemitic.sort_values(by='len_text' , ascending=False)[:3]
        longest_3_tweets_antisemitic = self.df_antisemitic.sort_values(by='len_text' , ascending=False)[:3]['Text'].tolist()
        longest_3_tweets_non_antisemitic= self.df_non_antisemitic.sort_values(by='len_text' , ascending=False)[:3]['Text'].tolist()

        res = {"antisemitic" : longest_3_tweets_antisemitic , "non_antisemitic" : longest_3_tweets_non_antisemitic}
        return res

    def get_all_word(self ):
        all_word = self.df["Text"].values
        return list(all_word)

    def get_dic_count_word(self):
        dic_res = {}
        for str in self.get_all_word():
            lst = str.strip().split()
            for word in lst:
                if word in dic_res:
                    dic_res[word] += 1
                else:
                    dic_res[word] = 1
        return dic_res

    def get_most_popular_word(self , num = 10):
        dic_count_word = self.get_dic_count_word()
        top_num_val = sorted(dic_count_word.items(), reverse=True, key=lambda x: x[1])[:num]
        return [x[0] for x in top_num_val]

    def get_all_word_by_df(self , df , column_name = 'Text'):
        all_word = df[column_name].values
        return list(all_word)

    def get_num__word_uppercase(self , df , column_name = 'Text'):
        all_word = self.get_all_word_by_df(df , column_name)
        counter_uppercase = 0
        for sent in all_word:
            lst = sent.strip().split()
            for word in lst:
                if word.isupper():
                    counter_uppercase+=1
        return counter_uppercase

    def get_resulot_json(self):
        dic_caount = self.count_from_category()
        dic_average = self.evrage_words_tweest()
        dic_longest_tweest = self.longest_3_tweets()
        dic = {"total_tweets" :{"antisemitic": dic_caount[1], "non_antisemitic": dic_caount[0],
                "total": dic_caount[0] + dic_caount[1] } ,
            "average_length": {
                "antisemitic": dic_average["average_df_antisemitic"],
                "non_antisemitic": dic_average["average_df_non_antisemitic"],
                "total": dic_average["total"]
            },
           "common_words": {
               "total": self.get_most_popular_word(num=10)
           } ,
            "longest_3_tweets" :{"antisemitic" : dic_longest_tweest["antisemitic"] , 'non_antisemitic' : dic_longest_tweest['non_antisemitic']} ,
            'uppercase_words' : {"antisemitic" : self.get_num__word_uppercase(self.df_antisemitic) , "non_antisemitic" : self.get_num__word_uppercase(self.df_non_antisemitic) , "total" : self.get_num__word_uppercase(self.df)}
           }
        return dic


# #
# a = Data_investigation(pd.read_csv(r"../data/tweets_dataset.csv"))
#
# print(a.count_from_category())
# print("Aaa")
# print("Aa")
# print(a.evrage_words_tweest())
# print("!!!!!!!!111")
# # print(a.longest_3_tweets()["antisemitic"][0])
# # print(df['Text'][6870])
#
# # print(a.get_dic_count_word())
# # prices = {
# #     "banana": 1.20,
# #     "pineapple": 0.89,
# #    "apple": 1.57,
# #    "grape": 2.45,
# #  }
# #
# # a= list(prices.values())
# # b =sorted(a , reverse=True)
# # print(list(prices.values()) )
# # print(b)
#
# # print(a.get_most_popular_word())
# # print(a.get_num__word_uppercase(a.df_antisemitic))
# # print(a.get_num__word_uppercase(a.df_non_antisemitic))
# # print(a.get_num__word_uppercase(a.df))
# print(a.get_resulot_json())