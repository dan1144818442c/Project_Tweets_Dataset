import pandas as pd
class cleaner:
    def __init__(self , df):
        self.df=  df
        self.clean_df = self.save_specific_column()


    def save_specific_column(self , lst_name = ['Text' ,'Biased']):
        df = self.df[lst_name]
        return df

    @staticmethod
    def Removing_punctuation_marks( df):
        df = df.copy()
        df["Text"]= df["Text"].transform(lambda x : x.replace("," , " "))
        return df

    @staticmethod
    def change_to_lower(df ):
        df = df.copy()
        df["Text"] = df["Text"].transform(lambda x: x.lower())
        return df

    @staticmethod
    def Removing_uncategorized_tweets(df):
        df = df.copy()
        df["good_Biased"] = df["Biased"].transform(lambda x:  x in [0,1]   )

        df = df[df["good_Biased"] == True]
        return df.drop(columns="good_Biased")



#
# a = cleaner(r"C:\Users\1\Desktop\DATA_Analiza\project_tweets_dataset\data\tweets_dataset.csv")
# print(a.clean_df)
# print("AAa")
# print(a.Removing_punctuation_marks())
# print(a.chane_to_lower())
# print("AAAAAAAAAAAaaa")
# print(a.Removing_uncategorized_tweets())