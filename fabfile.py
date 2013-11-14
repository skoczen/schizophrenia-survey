from fabric.api import *

env.PROJECT_NAME = "schizophrenia-survey"
env.GITHUB_USER = "skoczen"
env.GITHUB_REPO = env.PROJECT_NAME
env.VIRTUALENV_NAME = env.PROJECT_NAME
env.HEROKU_APP_NAME = env.PROJECT_NAME
# If you're using https://github.com/ddollar/heroku-accounts
env.HEROKU_ACCOUNT = "personal"
env.app_string = ""

env.SERVERS = {
    "live": "qi-schizophrenia-live",
    "staging": "qi-schizophrenia-staging",
}


def refreeze():
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; pip install -r requirements.unstable.txt" % env)
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate; pip freeze requirements.unstable.txt > requirements.txt" % env)


def run_ve(cmd):
    env.cmd = cmd
    local("source ~/.virtualenvs/%(VIRTUALENV_NAME)s/bin/activate;%(cmd)s" % env)


def deploy(target="staging"):
    env.app_string = "--app %s" % env.SERVERS[target]
    run_ve("./manage.py collectstatic --noinput --settings=envs.live" % env)
    run_ve("./manage.py compress --force --settings=envs.live" % env)
    run_ve("./manage.py sync_static --gzip --expires --settings=envs.live" % env)
    deploy_code()


def deploy_code():
    run_ve("git push heroku master:master" % env)
    run_ve("heroku run manage.py syncdb --settings=envs.live" % env)
    run_ve("heroku run manage.py migrate --settings=envs.live" % env)
    run_ve("heroku restart")
