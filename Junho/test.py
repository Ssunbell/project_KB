import pandas as pd
import numpy as np

from glob import glob
from tqdm import tqdm
from scipy import interpolate

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, GRU, AveragePooling1D, GlobalAveragePooling1D, Dropout, Conv1D
root = '/Users/junho/Desktop/git_repo/KB'
import pdfplumber as pdf
doc = pdf.open(f'{root}/src/src.pdf')
len(doc.pages)
sents = [doc.pages[i].extract_text().split('\n') for i in range(len(doc.pages))]

doc_sents = []
for i in sents:
    doc_sents.extend(i)

doc_sents = [i.replace(',',' ').strip() for i in doc_sents]

origin = ''
for i in doc_sents:
    origin += i

origin