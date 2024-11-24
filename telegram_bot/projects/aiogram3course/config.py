import os.path

from environs import Env

env = Env()
env.read_env(os.path.join(os.path.dirname(__file__), 'envs/.env'))

BOT_TOKEN = env.str('BOT_TOKEN')
