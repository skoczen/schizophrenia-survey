from memcacheify import memcacheify
from postgresify import postgresify
from envs.common import *

DATABASES = None
DATABASES = postgresify()
