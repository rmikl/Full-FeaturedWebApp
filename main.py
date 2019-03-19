from flask import Flask, render_template, url_for


app = Flask(__name__)



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
def hello():
    return render_template('home.html', title='Strona Glowna')

@app.route("/about")
def about():
    return render_template('about.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)