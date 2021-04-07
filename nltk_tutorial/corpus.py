import os, os.path
import nltk.data
from pathlib import Path

path = os.path.expanduser('~/nltk_data')
print(path)
print(path in nltk.data.path)

own_path = Path(os.path.dirname(__file__)).parent
data_path_original = os.path.join(own_path, 'data_march2020\\14dayquarantine.csv')
print(own_path in nltk.data.path)
print(nltk.data.path)
nltk.data.path.append(own_path)
print(nltk.data.path)