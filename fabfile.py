from fabric.api import env, run, prefix, cd, local

env.user = 'vokal'
env.hosts = ['tango.johan.cc']
env.directory = '/home/vokal/srv/vokalforeningen'
env.activate = 'source /home/vokal/.virtualenvs/vokalforeningen/bin/activate'

def deploy():
    local('git push')
    with cd(env.directory):
        with prefix(env.activate):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py collectstatic')
            run('touch vokalforeningen/wsgi.py') # this triggers a gracefull reload
