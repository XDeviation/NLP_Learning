import pandas as pd
from matplotlib import pyplot as plt

datapath = '../../data/train_set.csv'

train_df = pd.read_csv(datapath, sep='\t', nrows=100)

train_df['text_len'] = train_df['text'].apply(lambda x: len(x.split(' ')))
print(train_df['text_len'].describe())
