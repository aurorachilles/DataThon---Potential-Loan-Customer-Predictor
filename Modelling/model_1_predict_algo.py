import pandas as pd
import numpy as np


# This model is built purely based upon the given data without any alterations. 
# Only duplicates are removed and misisng values are imputed.
# There were no duplicates or misisng values so proceeding directly with the analysis

# The primary objective of this initial model is to find out which is the best Algo for the analysis

#reading data form csv
data = pd.read_csv("../Dataset/loan_dataset.csv")

#dropping unnecessary columns
data = data.drop(['Unnamed: 0'],axis=1)

