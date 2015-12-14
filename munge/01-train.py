'''
Munges train data.

Authors:
Paul Hendricks

Date:
2016-01-08

inputs:
train.csv.zip

outputs:
train.h5
'''


# Load libraries
import pandas as pd
import zipfile
import numpy as np

# Load data
original_path = './data/original/'
file_name = 'train.csv'
z = zipfile.ZipFile(original_path + file_name + '.zip')
train = pd.read_csv(z.open(file_name))

# TODO Set column names

# TODO Set column types

# TODO Filter out certain columns

# TODO Filter out certain observations

# TODO Ensure uniqueness at some level

# TODO Define other variables

# TODO Write out data to data/prepped/
prepped_path = './data/prepped/'
train.to_hdf(prepped_path + file_name + '.h5', 'table', append=True)
