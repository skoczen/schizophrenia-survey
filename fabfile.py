from fabric.api import *

env.PROJECT_NAME = "schizophrenia-survey"
env.GITHUB_USER = "skoczen"
env.GITHUB_REPO = env.PROJECT_NAME
env.VIRTUALENV_NAME = env.PROJECT_NAME
env.HEROKU_APP_NAME = env.PROJECT_NAME
# If you're using https://github.com/ddollar/heroku-accounts
env.HEROKU_ACCOUNT = "personal"
env.app_string = ""
env.DEV_DB_URL = "postgres://@localhost:5432/schizophrenia"

env.SERVERS = {
    "live": "qi-schizophrenia-live",
    "staging": "qi-schizophrenia-staging",
}


def refreeze():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; pip install -r requirements.unstable.txt" % env)
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; pip freeze requirements.unstable.txt > requirements.txt" % env)

def deploy(target="staging"):
    env.app_string = "--app %s" % env.SERVERS[target]
    local("git push heroku master:master" % env)
    local("heroku run python manage.py syncdb --migrate --settings=envs.live %(app_string)s" % env)
    local("heroku restart %(app_string)s" % env)
