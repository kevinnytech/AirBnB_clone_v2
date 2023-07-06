#!/usr/bin/python3
"""
Fabric script (based on the file 2-do_deploy_web_static.py) that creates
and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import local, run, env, cd, put
from datetime import datetime
import os

env.hosts = ['52.201.190.14', '54.160.65.122']
env.user = "ubuntu"


def do_pack():
    """ Generates a .tgz archive """
    try:
        if not os.path.exists('versions'):
            local('mkdir versions')
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} ./web_static".format(file_name))
        return file_name
    except Exception:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if (os.path.exists(archive_path) is False):
        return False
    filename = '/data/web_static/releases/{}'.format(
        archive_path.strip(".tgz"))
    archive = archive_path.lstrip('versions/')
    run('mkdir -p {}'.format(filename))
    # run('mkdir /tmp/versions')
    put('{}'.format(archive_path), "/tmp/")
    run('tar -xzf /tmp/{} -C {}'.format(archive, filename))
    run('mv {}/web_static/* {}'.format(filename, filename))
    run('rm -rf {}/web_static/'.format(filename))
    run('rm /tmp/{}'.format(archive))
    run('rm /data/web_static/current')
    run('ln -sf {} /data/web_static/current'.format(filename))
    return True


def deploy():
    """ Deploy to your web servers """
    archive_path = do_pack()
    return do_deploy(archive_path) if archive_path else False
