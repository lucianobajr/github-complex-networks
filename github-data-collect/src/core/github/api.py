from github import Github

class GithubApi:
    def __init__(self, token:str) -> None:
        self.instance = Github(token)
