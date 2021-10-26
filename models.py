import json

def getRepos():
    with open("data/repos.json") as f:
        return json.load(f)

def getCommits():
    with open("data/commits.json") as f:
        return json.load(f)