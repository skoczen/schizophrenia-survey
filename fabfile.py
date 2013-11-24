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


def local_venv(cmd):
    env.cmd = cmd
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; %(cmd)s" % env)


def refreeze():
    local_venv("pip install -r requirements.unstable.txt")
    local_venv("pip freeze requirements.unstable.txt > requirements.txt")


def deploy(target="staging"):
    env.app_string = "--app %s" % env.SERVERS[target]
    local("git push heroku master:master" % env)
    local("heroku run python manage.py syncdb --migrate --settings=envs.live %(app_string)s" % env)
    local("heroku restart %(app_string)s" % env)


def unit():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; manage.py test --attr=\!e2e" % env)


def e2e():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; manage.py test --attr=\!e2e" % env)


def wip():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; manage.py test --attr=wip" % env)


def setup_db():
    local_venv("dropdb schizophrenia --if-exists")
    local_venv("createdb schizophrenia")
    local_venv("./manage.py syncdb --noinput")
    local_venv("./manage.py loaddata permissions.json")
    local_venv("./manage.py loaddata dev_user.json")
    local_venv("./manage.py migrate")
    local_venv("./manage.py fake_db")
