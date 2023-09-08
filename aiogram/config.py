from envparse import env

env.read_envfile()

BOT_TOKEN = env.str('BOT_TOKEN')
HF_TOKEN = env.str('HF_TOKEN')
CHECKPOINT = env.str('CHECKPOINT')
MODEL_API = env.str('MODEL_API')
