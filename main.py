from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm



app = Flask(__name__)
app.config['SECRET_KEY'] = '74eed421a8148c400b26d6f3e2319147'


posts = [
    {
        'autor':'Root',
        'tytul':'Pierwszy Post',
        'zawartosc':'testowa zawartosc',
        'data':'18-03-2019'
    },
    {
        'autor':'Root',
        'tytul': 'drugi Post',
        'zawartosc': 'testowa zawartosc',
        'data': '19-03-2019'
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title='Strona Glowna')

@app.route("/about")
def about():
    return render_template('about.html', posts=posts)

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
            flash( str({form.username.data}) + 'zostal poprawnie zarejestowany!', 'success')
            return(redirect(url_for('home')))
    return render_template('register.html', title='Zarejestruj', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Zaloguj', form=form)



if __name__ == '__main__':
    app.run(debug=True)