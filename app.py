from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_Key'


class LoginForm(FlaskForm):
    username = StringField('username')
    gender = SelectField('gender', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    password = PasswordField('password')

@app.route('/form', methods=['POST','GET'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h2>username is {} password is {}'.format(form.username.data, form.password.data)
    return render_template('form.html',form = form)

if __name__ == '__main__':
    app.run(debug=True)
