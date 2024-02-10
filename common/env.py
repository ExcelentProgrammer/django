import os

import environ

environ.Env.read_env(os.path.join('.env'))

#####################
# Env uchun default qiymatlarni shu yerda berish kerak
#####################
env = environ.Env(
    debug=(bool, False),
    CACHE_TIME=(int, 180)
)
