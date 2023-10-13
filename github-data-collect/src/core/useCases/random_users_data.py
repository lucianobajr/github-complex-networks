import random

import pandas as pd

from config.environments import MAIN_TOKEN_GITHUB

from constants.csv_header import csv_header
from constants.paths import base_path_random_data,initial_data_path

from core.csv.manager import ManagerCSV
from core.github.api import GithubApi

class RandomUsersData:
    def __init__(self,num_random_users:int) -> None:
        self.api = GithubApi(token=MAIN_TOKEN_GITHUB)
        self.num_random_users = num_random_users

    def generate_random_users(self):
        df = pd.read_csv(initial_data_path, encoding='utf-8')

        # Lista para armazenar os usuários aleatórios
        random_users = set()  # Use um conjunto para evitar repetições


        # Itere para coletar o número desejado de usuários aleatórios
        while len(random_users) < self.num_random_users:
            # Gere um índice aleatório
            
            df_len = len(df) -1
            random_index = random.randrange(0,df_len)

            row = df.iloc[random_index]
            
            # Recupere a lista de following_users e followers_users
            following_users = str(row["Following Users"]).split(", ")
            followers_users = str(row["Followers Users"]).split(", ")
            
            # Gere um usuário candidato aleatório a partir das listas de following e followers
            candidates = set(following_users + followers_users)
            valid_candidates = [candidate for candidate in candidates if candidate not in df['Nome de usuário'].values and candidate not in random_users]
            
            if valid_candidates:
                random_candidate_login = random.choice(valid_candidates)
                random_candidate = self.api.instance.get_user(random_candidate_login)
                random_users.add(random_candidate)


        return random_users

    def Boostrap(self):
        random_users = self.generate_random_users()

        csv_filename = base_path_random_data + str(self.num_random_users) +".csv"

        # Crie uma instância do ManagerCSV
        csv_manager = ManagerCSV(csv_filename, header=csv_header)

        # Escreva o cabeçalho
        csv_manager.write_header()

        for random_user in random_users:  
            following_users = [u.login for u in random_user.get_following()]
            followers_users = [u.login for u in random_user.get_followers()]

            user_info = [
                random_user.login,
                random_user.id,
                random_user.avatar_url,
                random_user.gravatar_id,
                random_user.url,
                random_user.html_url,
                random_user.followers_url,
                random_user.following_url,
                random_user.gists_url,
                random_user.starred_url,
                random_user.subscriptions_url,
                random_user.organizations_url,
                random_user.repos_url,
                random_user.events_url,
                random_user.received_events_url,
                random_user.type,
                random_user.site_admin,
                random_user.name,
                random_user.company,
                random_user.blog,
                random_user.location,
                random_user.email,
                random_user.hireable,
                random_user.bio,
                random_user.public_repos,
                random_user.public_gists,
                len(followers_users),
                len(following_users),
                random_user.created_at,
                random_user.updated_at,
                ", ".join(following_users),  # Combine following users into a string
                ", ".join(followers_users),  # Combine followers users into a string
            ]
            csv_manager.write_data(user_info)

        print(f"User information saved to {csv_filename}")