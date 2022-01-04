from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Anoop KS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'Anju R',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2021'
    }
]

@app.route("/home")
@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title = 'About')

if __name__ == '__main__':
    app.run(debug=True)