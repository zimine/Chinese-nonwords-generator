import pandas as pd
import numpy as np
import random
from pypinyin import pinyin, lazy_pinyin, Style

subset = pd.read_csv('data/subset.csv')
word = pd.read_csv('data/word.csv')
word_phon = word['pinyinword'].value_counts().to_dict()

def generate_nonwords(stroke_min, stroke_max, num_nei_min, num_nei_max, logfreq_min, logfreq_max, N, random_state=42):
    stroke_mask = (subset['Stroke'] >= stroke_min) & (subset['Stroke'] <= stroke_max)
    num_nei_mask = (subset['Num-neighbor'] >= num_nei_min) & (subset['Stroke'] <= num_nei_max)
    logfreq_mask = (subset['C&B_log'] >= logfreq_min) & (subset['C&B_log'] <= logfreq_max)
    select = subset.loc[(stroke_mask) & (num_nei_mask) & (logfreq_mask)]
    sample = select.sample(n=2*N, random_state=random_state)
    return sample

def get_randomized_words(sample):
    N = sample.shape[0]
    df = pd.DataFrame()
    char_1 = []
    char_2 = []
    logfreq_1 = []
    logfreq_2 = []
    stroke_1 = []
    stroke_2 = []
    hd_1 = []
    hd_2 = []
    numnei_1 = []
    numnei_2 = []
    for i in np.arange(0, N, 2):
        nonword_pinyin = ''.join(lazy_pinyin(sample.iloc[i]['Char']+sample.iloc[i+1]['Char']))
        if nonword_pinyin not in word_phon.keys():
            char_1.append(sample.iloc[i]['Char'])
            char_2.append(sample.iloc[i+1]['Char'])
            logfreq_1.append(sample.iloc[i]['C&B_log'])
            logfreq_2.append(sample.iloc[i+1]['C&B_log'])
            hd_1.append(sample.iloc[i]['HD'])
            hd_2.append(sample.iloc[i+1]['HD'])
            numnei_1.append(sample.iloc[i]['Num-neighbor'])
            numnei_2.append(sample.iloc[i+1]['Num-neighbor'])
            stroke_1.append(sample.iloc[i]['Stroke'])
            stroke_2.append(sample.iloc[i+1]['Stroke'])
    df['Char-1'] = char_1
    df['Char-2'] = char_2
    df['Logfreq-1'] = logfreq_1
    df['Logfreq-2'] = logfreq_2
    df['Stroke-1'] = stroke_1
    df['Stroke-2'] = stroke_2
    df['HD-1'] = hd_1
    df['HD-2'] = hd_2
    df['NumNeighbor-1'] = numnei_1
    df['NumNeighbor-2'] = numnei_2
    return df







