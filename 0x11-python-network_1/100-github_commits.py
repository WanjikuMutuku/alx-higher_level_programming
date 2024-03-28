#!/usr/bin/python3
"""takes 2 arguments in order to solve this challenge."""
import requests
import sys


def get_commits(repository, owner):
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 100-github_commits.py <repository> <owner>")
        sys.exit(1)

    repository = sys.argv[1]
    owner = sys.argv[2]
    get_commits(repository, owner)
