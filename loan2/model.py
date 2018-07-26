from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd
import pickle
dataset = pd.read_csv('clean_dataset.csv')
X = dataset[['Current Loan Amount', 'Term', 'Credit Score', 'Annual Income', 'Years in current job', 'Home Ownership', 'Purpose', 'Monthly Debt', 'Years of Credit History',
             'Months since last delinquent', 'Number of Open Accounts', 'Number of Credit Problems', 'Current Credit Balance', 'Maximum Open Credit', 'Bankruptcies', 'Tax Liens']]
y = dataset['Loan Status']

sc_X = StandardScaler()
sc_X.fit(X, y)
X = sc_X.transform(X)

pickle.dump(sc_X, open('finalized_scaler.sav', 'wb'))

logistic_classifier = LogisticRegression()
logistic_classifier.fit(X, y)
pickle.dump(logistic_classifier, open('finalized_model.sav', 'wb'))
