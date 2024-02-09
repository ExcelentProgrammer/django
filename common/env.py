import os

import environ

environ.Env.read_env(os.path.join('.env'))

env = environ.Env(
    debug=(bool, False),
    CACHE_TIME=(int, 180)
)
