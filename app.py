from flask import Flask, render_template, url_for
import time
import models

app = Flask(__name__)

@app.route('/')
def index():
    repos = models.getRepos()
    commits = models.getCommits()
    time_tags = {}
    for c in commits['commits']:
        c['time_since'] = int(time.time()) - c['time_since']
        if c['time_since'] // 60 == 0:
            time_tags[c['hash']] = "seconds"
        elif c['time_since'] // 3600 == 0:
            time_tags[c['hash']] = "minutes"
            c['time_since'] = c['time_since'] % 60
        elif c['time_since'] // (3600 * 24) == 0:
            time_tags[c['hash']] = "hours"
            c['time_since'] = c['time_since'] % 60 % 60
        elif c['time_since'] // (3600 * 24 * 30) == 0:
            time_tags[c['hash']] = "days"
            c['time_since'] = c['time_since'] % 60 % 60 % 24
        else:
            time_tags[c['hash']] = "months"
            c['time_since'] = c['time_since'] % 60 % 60 % 24 % 30
    return render_template('index.html', repos=repos['repos'], commits=commits['commits'][::-1], time_tags=time_tags)

@app.route('/<repo_hash>')
def repo(repo_hash):
    return render_template('repo.html')

if __name__ == '__main__':
    app.run()