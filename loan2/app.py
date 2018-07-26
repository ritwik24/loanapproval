from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, FloatField
from wtforms.validators import InputRequired
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_Key'
class LoginForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    current_loan_amount = FloatField('Current Loan Amount', validators=[InputRequired()])
    term = SelectField('Term', choices=[
                         ('1', 'Long'), ('0', 'Short')], validators=[InputRequired()])
    credit_score = FloatField('Cibil Score', validators=[InputRequired()])
    annual_income = FloatField('Annual Income', validators=[InputRequired()])
    years_in_current_job = SelectField('Years in Current Job', choices=[(
        '0', '<1'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10+')], validators=[InputRequired()])
    home_ownership = SelectField('Home Ownership', choices=[
                         ('0', 'Home Mortgage'), ('1', 'Rent'), ('2', 'Own Home'), ('3', 'Have Mortgage')], validators=[InputRequired()])
    purpose = SelectField('Purpose', choices=[
                         ('0', 'Debt Consolidation'), ('2', 'Home Improvements'), ('3', 'Business Loan'), ('4', 'Buy A Car'), ('5', 'Medical Bills'), ('6', 'Buy House'), ('7', 'Take a Trip'), ('8', 'Major-purchases'), ('9', 'Small-Business'), ('10', 'Moving'), ('11', 'Wedding'), ('12', 'Vacation'), ('13', 'Educational Expenses'), ('14', 'renewable Energy'), ('1', 'Other')], validators=[InputRequired()])
    monthly_debt =  FloatField('Monthly Debt', validators=[InputRequired()])
    years_of_credit_history =  FloatField('Years of Credit History', validators=[InputRequired()])
    months_since_last_delinquent = FloatField('Months since last delinquent', validators=[InputRequired()])
    number_of_open_accounts = FloatField('Number of Open Accounts', validators=[InputRequired()])
    number_of_credit_problems = FloatField('Number of Credit Problems', validators=[InputRequired()])
    current_credit_balance = FloatField('Current Credit Balance', validators=[InputRequired()])
    maximum_open_credit = FloatField('Maximum Open Account', validators=[InputRequired()])
    bankruptcies = FloatField('Bankruptcies', validators=[InputRequired()])
    tax_liens = FloatField('Tax Liens', validators=[InputRequired()])
 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['POST','GET'])
def form():
    form = LoginForm()
    if request.method == "POST":
        data = request.form.to_dict()
        # print(data)
        if form.validate_on_submit():
            input_data = data.copy()
            input_data.pop('csrf_token',None)
            input_data.pop('name',None)
            input_data = pd.DataFrame(input_data,index=['0'], columns=['current_loan_amount', 'term', 'credit_score', 'annual_income', 'years_in_current_job', 'home_ownership', 'purpose','monthly_debt','years_of_credit_history','months_since_last_delinquent','number_of_open_accounts','number_of_credit_problems','current_credit_balance','maximum_open_credit','bankruptcies','tax_liens'])
            input_data.to_csv('inputdata2.csv')
            scaler = pickle.load(open('finalized_scaler.sav', 'rb'))
            model = pickle.load(open('finalized_model.sav', 'rb'))
            result = model.predict(scaler.transform(input_data))
            # print(result)
            return render_template("result.html", result = result[0])
    return render_template('form.html',form = form)


if __name__ == '__main__':
    app.run(debug=True)
