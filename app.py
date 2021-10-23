from flask import Flask, render_template, url_for
import models

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/<repo_name>')
def repo(repo_name):
    r = models.getRepo(repo_name)
    return render_template('repo.html', repo=r)

if __name__ == '__main__':
    app.run()