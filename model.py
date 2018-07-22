import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

data = pd.read_csv('dataset.csv')
X = data[['Gender_Male', 'Married_Yes', 'Education_Not Graduate', 'Self_Employed_Yes', 'Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', ]]
y = data['Loan_Status']
sc_X = StandardScaler()
sc_X.fit(X)
X = sc_X.transform(X)

pickle.dump(sc_X, open('finalized_scaled.sav', 'wb'))

from sklearn.linear_model import LogisticRegression
logistic = LogisticRegression()
logistic.fit(X,y)

filename = 'finalized_model.sav'
pickle.dump(logistic, open(filename, 'wb'))
