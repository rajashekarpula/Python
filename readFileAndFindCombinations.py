



import pandas as pd
import itertools as it
from pandas import compat

filePath = raw_input("Please enter the relative path of the file")
fileData = pd.read_csv(filePath)
dataDict = {}

print fileData


def to_dict_dropna(data):
  return dict((k, v.dropna().to_dict()) for k, v in compat.iteritems(data))
dataDict = to_dict_dropna(fileData)

def expand_grid(data_dict):
	rows = it.product(*data_dict.values())
	return pd.DataFrame.from_records(rows, columns=data_dict.keys())

df = expand_grid(dataDict)

df.to_csv("output.csv",index=False)

print df