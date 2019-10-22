# Homework 2 Jing Xu
# T1. Write a python reads creates a dataframe from a URL that points to a CSV file
import pandas as pd


def read_and_create(data_url):
    data = pd.read_csv(data_url)
    return data


# T2. Create the function test_create_dataframe that takes as input:
# (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold
# The DataFrame contains only the columns that you specified as the second argument.
# The values in each column have the same python type
# There are at least 10 rows in the DataFrame.
def test_create_dataframe(dataframe, columns_names):
    if dataframe.shape[0] < 10:
        return False
    if list(dataframe.columns) != columns_names:
        return False
    for i in columns_names:
        for j in dataframe[i]:
            if type(j) != type(dataframe[i][0]):
                return False
    return True




