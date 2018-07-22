from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, FloatField
from wtforms.validators import InputRequired
import model
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_Key'


class LoginForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    dependents = SelectField('Dependents', choices=[(
        '0', '0'), ('1', '1'), ('2', '2'), ('3', '3+')], validators=[InputRequired()])
    applicant_income = FloatField(
        'Applicant Income', validators=[InputRequired()])
    gender = SelectField('Gender', choices=[
                         ('1', 'Male'), ('0', 'Female')], validators=[InputRequired()])
    married = SelectField('Married', choices=[
                         ('1', 'Yes'), ('0', 'No')], validators=[InputRequired()])
    education = SelectField('Education', choices=[(
        '0', 'Graduate'), ('1', 'Not Graduate')], validators=[InputRequired()])
    self_employed = SelectField('Selfemployed', choices=[
                         ('1', 'Yes'), ('0', 'No')], validators=[InputRequired()])
    
    
    
    coapplicant_income = FloatField('Coapplicant Income', validators=[InputRequired()])
    
    loan_amount = FloatField('Loan Amount', validators=[InputRequired()])
    loan_amount_term = FloatField('Loan Amount Term', validators=[InputRequired()])
    credit_history = SelectField('Credit History', choices=[(
        '0', 'Nil'), ('1', 'Yes')], validators=[InputRequired()])
    property_area = SelectField('Property Area', choices=[(
        '0', 'Urban'), ('1', 'Rural'), ('2', 'Semi Urban')], validators=[InputRequired()])


@app.route('/form', methods=['POST','GET'])
def form():
    form = LoginForm()
    if request.method == "POST":
        data = request.form.to_dict()
        print(data)
        if form.validate_on_submit():
            input_data = data.copy()
            input_data.pop('csrf_token',None)
            input_data.pop('name',None)
            input_data = pd.DataFrame(input_data,index=['0'], columns=['dependents', 'applicant_income', 'coapplicant_income','loan_amount','loan_amount_term','credit_history','property_area','gender','married','education','self_employed'])
            input_data.to_csv('inputdata2.csv')
            result = model.logistic.predict(
                model.sc_X.transform(input_data))
            print(result)
            return 'Data {}'.format(result)
    return render_template('form.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)
