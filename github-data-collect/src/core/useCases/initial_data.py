from config.environments import MAIN_TOKEN_GITHUB

from constants.csv_header import csv_header
from constants.paths import base_initial_data_path

from core.csv.manager import ManagerCSV
from core.github.api import GithubApi

class InitialData:
    def __init__(self,username:str) -> None:
        self.api = GithubApi(token=MAIN_TOKEN_GITHUB)
        self.username = username

    def user_following(self):
        # Get the user object for the user you want to check
        user = self.api.instance.get_user(self.username)

        # Get the list of users that the specified user is following
        following = user.get_following()

        return following

    def Boostrap(self):
        csv_filename = base_initial_data_path + self.username + ".csv"

        # Crie uma instância do ManagerCSV
        csv_manager = ManagerCSV(csv_filename, header=csv_header)

        # Escreva o cabeçalho
        csv_manager.write_header()

        following = self.user_following()

        for user in following:
            following_users = [u.login for u in user.get_following()]
            followers_users = [u.login for u in user.get_followers()]
            
            user_info = [
                user.login,
                user.id,
                user.avatar_url,
                user.gravatar_id,
                user.url,
                user.html_url,
                user.followers_url,
                user.following_url,
                user.gists_url,
                user.starred_url,
                user.subscriptions_url,
                user.organizations_url,
                user.repos_url,
                user.events_url,
                user.received_events_url,
                user.type,
                user.site_admin,
                user.name,
                user.company,
                user.blog,
                user.location,
                user.email,
                user.hireable,
                user.bio,
                user.public_repos,
                user.public_gists,
                len(followers_users),
                len(following_users),
                user.created_at,
                user.updated_at,
                ", ".join(following_users),  # Combine following users into a string
                ", ".join(followers_users),  # Combine followers users into a string
            ]
            
            csv_manager.write_data(user_info)

        print(f"Users information saved to {csv_filename}")