import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('dataset.csv')
X = data[['Dependents', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
              'Credit_History', 'Property_Area', 'Gender_Male', 'Married_Yes', 'Education_Not Graduate', 'Self_Employed_Yes']]
y = data['Loan_Status']
sc_X = StandardScaler()
sc_X.fit(X)
X = sc_X.transform(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
randomforrestclassifier = RandomForestClassifier(n_estimators=61)
randomforrestclassifier.fit(X_train, y_train)
print(randomforrestclassifier.score(X_test, y_test))
