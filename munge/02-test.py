import pandas as pd


test = pd.read_csv("../data/original/test.csv")

test.to_csv("../data/prepped/test.csv")
