import json

def getRepos():
    with open("data/repos.json") as f:
        return json.load(f)

def getRepo(hash):
    with open("data/repos.json") as f:
        repos = json.load(f)['repos']
        for r in repos:
            if r['hash'] == hash:
                return r

def getCommits():
    with open("data/commits.json") as f:
        return json.load(f)

def getKeys():
    with open("data/keys.json") as f:
        return json.load(f)