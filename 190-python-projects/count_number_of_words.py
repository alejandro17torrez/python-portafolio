import logging

import pandas as pd

logging.basicConfig(level=logging.DEBUG)


data = pd.read_csv(
    "https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv",
    encoding="latin1",
)


def get_count_of_words_by_column(column: str, dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Get the count of words by column in a dataframe of Pandas

    Parameters:
        column: str
        dataframe: DataFrame

    Return:
        dataframe with new column with the count of words of selected column
    """
    try:
        return dataframe[f"{column}"].apply(lambda string: len(string.split()))
    except TypeError:
        print(
            "Invalid type, the Parameters should be column: str and dataframe: DateFrame"
        )


data["Article length"] = get_count_of_words_by_column(column="Article", dataframe=data)
data["Title length"] = get_count_of_words_by_column(column="Title", dataframe=data)
logging.debug(data)
