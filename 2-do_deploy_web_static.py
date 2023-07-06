#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
import os
from fabric.api import run, env, cd, put
env.hosts = ['52.201.190.14', '54.160.65.122']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if (os.path.exists(archive_path) is False):
        return False
    filename = '/data/web_static/releases/{}'.format(
        archive_path.strip(".tgz"))
    archive = archive_path.lstrip('versions/')
    run('mkdir -p {}'.format(filename))
    put('{}'.format(archive_path), "/tmp/")
    run('tar -xzf /tmp/{} -C {}'.format(archive, filename))
    run('mv {}/web_static/* {}'.format(filename, filename))
    run('rm -rf {}/web_static/'.format(filename))
    run('rm /tmp/{}'.format(archive))
    run('rm /data/web_static/current')
    run('ln -sf {} /data/web_static/current'.format(filename))
    return True
