import cleaner
import Loader
import Data_investigation

# import Data_investigation
path  = "../data/tweets_dataset.csv"
df = Loader.loader.get_df(path)
cleaner = cleaner.cleaner(df)
clean_df = cleaner.change_to_lower(cleaner.clean_df)
clean_df = cleaner.Removing_uncategorized_tweets(clean_df)
clean_df = cleaner.Removing_punctuation_marks(clean_df)
print(clean_df)
Loader.loader.write_to_csv("../data/tweets_dataset_cleaned.csv" , clean_df)
dic_res = Data_investigation.Data_investigation(df).get_resulot_json()
print(dic_res)
print(type(dic_res))
Loader.loader.write_to_json("../data/results.json" , dic_res)