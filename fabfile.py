
REPOS = (('jlcaro','origin','master'),)
PROJECT = 'jlcaro'
PROJECT_DIR_BASE = '/var/django'

def production():
    "Configures Fabric to access Production Server"
    config.fab_hosts = ['jlcaro.com']
    config.repos = REPOS
    config.project = PROJECT

def staging():
    "Configures Fabric to access Staging Server (Localhost)"
    config.fab_hosts = ['localhost']
    config.repos = REPOS
    config.project = PROJECT

def reboot_apache():
    "Reboot Apache2 server."
    require('fab_hosts', provided_by=[production, staging])
    sudo("apache2ctl graceful")

def syncdb():
    "Runs SyncDB for the django project"
    require('fab_hosts',provided_by=[staging, production])
    require('project',provided_by=[staging, production])
    run("cd "+PROJECT_DIR_BASE+"/; python manage.py syncdb")

def migrate():
    "Runs Migrate for the django project"
    require('fab_hosts',provided_by=[staging,production])
    require('project',provided_by=[staging, production])
    run("cd "+PROJECT_DIR_BASE+"/; python manage.py migrate")

def git_pull():
    "Updates the repository"
    run('cd '+PROJECT_DIR_BASE+'/$(repo)/; git pull $(parent) $(branch)')

def git_reset():
    "Resets the repository to specified version."
    run("cd "+PROJECT_DIR_BASE+"/$(repo)/; git reset --hard $(hash)")

def pull():
    "Pulls from the remote GitRepo"
    require('fab_hosts', provided_by=[production,staging])
    require('repos',provided_by=[staging,production])
    for repo, parent, branch in config.repos:
        config.repo = repo
        config.parent = parent
        config.branch = branch
        invoke(git_pull)

def reset(repo, hash):
    """
    Reset all git repositories to specified hash.
    Usage:
        fab reset:repo=my_repo,hash=etcetc123
    """
    require("fab_hosts", provided_by=[production,staging])
    config.hash = hash
    config.repo = repo
    invoke(git_reset)

def deploy():
    """Deploys the project to the target enviroment"""
    require("fab_hosts", provided_by=[production,staging])
    invoke(pull)
    invoke(reboot_apache)

    
