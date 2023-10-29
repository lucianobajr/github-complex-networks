import pandas as pd
import requests
from config.environments import RESERVE_TOKEN_GITHUB, MAIN_TOKEN_GITHUB
from constants.csv_header_users_graph_stats_data import csv_header_users_graph_stats_data
from core.csv.manager import ManagerCSV
from core.github.api import GithubApi

class UserGraphStatsData:
    def __init__(self, graph_dataset: str) -> None:
        self.api = GithubApi(token=MAIN_TOKEN_GITHUB)
        self.graph_dataset = graph_dataset

    def stats(self, username) -> dict:
        token = RESERVE_TOKEN_GITHUB
        query = """
        {
        user(login: "%s") {
            contributionsCollection {
            totalCommitContributions
            totalIssueContributions
            totalPullRequestContributions
            }
        }
        }
        """ % username

        url = 'https://api.github.com/graphql'

        headers = {
            'Authorization': 'Bearer ' + token,
        }

        response = requests.post(url, json={'query': query}, headers=headers)

        data_stats = {
            "TotalCommits": 0,
            "TotalIssues": 0,
            "TotalPullRequests": 0,
        }

        if response.status_code == 200:
            data = response.json()
            try:
                contributions = data['data']['user']['contributionsCollection']
                data_stats["TotalCommits"] = contributions['totalCommitContributions']
                data_stats["TotalIssues"] = contributions['totalIssueContributions']
                data_stats["TotalPullRequests"] = contributions['totalPullRequestContributions']
            except Exception as e:
                print(f"Erro na consulta GraphQL: {e}")

        return data_stats

    def open_repos_user(self, username) -> int:
        user = self.api.instance.get_user(username)
        return user.public_repos

    def Boostrap(self):
        df = pd.read_csv(self.graph_dataset, encoding='utf-8')
        csv_filename = "../resources/data/graph_users_with_stats.csv"
        csv_manager = ManagerCSV(
            csv_filename, header=csv_header_users_graph_stats_data)
        csv_manager.write_header()

        users = df["Label"].tolist()

        for idx, user in enumerate(users):
            try:
                data_stats = self.stats(user)
                data_stats["PublicRepos"] = self.open_repos_user(user)

                user_info = [
                    idx,
                    user,
                    data_stats["TotalCommits"],
                    data_stats["TotalIssues"],
                    data_stats["TotalPullRequests"],
                    data_stats["PublicRepos"]
                ]
            except Exception as e:
                user_info = [idx, user, 0, 0, 0, 0]
                print(f"Erro com o usuário {user}: {e}")
            
            csv_manager.write_data(user_info)