import pandas as pd
import numpy as np
from bloomdata import helper_function as hf
from bloomdata import wallet


d = np.array([[4, 1], [7, 3], [2, 7], [5, 6], [7, 5],
              [4, 8], [3, 2], [0, 6], [6, 2], [8, 9]])
df = pd.DataFrame(d)
frac = 0.8


def test_tts_isdf():
    assert type(hf.train_test_split(df, frac)[0]) == type(df)


def test_tts_len():
    assert len(hf.train_test_split(df, frac)[0]) / len(df) == frac


def test_wallet():
    assert wallet.Wallet().balence == 0