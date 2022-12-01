## import
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import statsmodels
import numpy as np
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sn

## readcsv
data = pd.read_csv(r"D:/UCL_CODE/CASA0007/data/Seattle/listings.csv")
print(data)
data.info()

