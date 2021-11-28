import os

env = os.getenv('CURRENT_ENV', 'dev')

if env =='dev':
    from .dev import *
elif env == 'test':
    from .test import *
elif env == 'prod':
    from prod import *
