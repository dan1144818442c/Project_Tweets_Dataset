import pandas as pd
import json

class loader:
    @staticmethod
    def get_df( path):
        return pd.read_csv(path)

    @staticmethod
    def write_to_csv(path , df ):
        with open(path , "w") as f:
            df.to_csv(path)

    @staticmethod
    def write_to_json(path , json_ ):
        with open(path , "w") as f:
            json.dump(json_  ,f)
