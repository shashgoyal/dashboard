from flask import Flask,request, render_template,flash,redirect,url_for,session,logging
from wtforms import Form, StringField,TextAreaField,PasswordField, validators

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

class changebankform(Form):
    name =StringField('Change Bank Name',[validators.Length(min=1,max=50)])
    username = StringField('Change Username', [validators.Length(min=4, max=50)])
    email = StringField('Change Bank Email', [validators.Length(min=8, max=50)])
    password=PasswordField('change password', [
        validators.DataRequired(),
        validators.EqualTo('confirm',message='passwords do not match')
    ])
    confirm=PasswordField('confirm password')

@app.route('/dashboard/modifydetails', methods=['GET', 'POST'])
def changebankinfo():
    form=changebankform(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('modify_bank.html')
    return render_template('modify_bank.html',form=form)



if __name__ == '__main__':
    app.run(debug=True)
