'''
Munges test data.

Authors:
Paul Hendricks

Date:
2016-01-08

inputs:
test.csv.zip

outputs:
test.h5
'''


# TODO Load libraries
import pandas as pd
import zipfile
import numpy as np

# TODO Load data
original_path = './data/original/'
file_name = 'test.csv'
z = zipfile.ZipFile(original_path + file_name + '.zip')
test = pd.read_csv(z.open(file_name))
test.head()

# TODO Set column names

# TODO Set column types

# TODO Filter out certain columns

# TODO Filter out certain observations

# TODO Ensure uniqueness at some level

# TODO Define other variables

# TODO Write out data to data/prepped/
prepped_path = './data/prepped/'
test.to_hdf(prepped_path + file_name + '.h5', 'table', append=True)
