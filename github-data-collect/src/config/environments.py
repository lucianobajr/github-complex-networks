from dotenv import load_dotenv
import os

load_dotenv()

MAIN_TOKEN_GITHUB = os.getenv('MAIN_TOKEN_GITHUB')
RESERVE_TOKEN_GITHUB = os.getenv('RESERVE_TOKEN_GITHUB')
INITIAL_USER = os.getenv('INITIAL_USER')