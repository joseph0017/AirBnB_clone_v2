#!/usr/bin/python3
"""This module defines a function that generates an archive of contents of
web_static folder"""


from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['100.26.17.152', '54.89.109.11']
env.user = 'ubuntu'
env.key_file_name = '~/.ssh/id_rsa'


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -cvzf {} web_static".format(filename))
    return filename


def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
        put(archive_path, "/tmp/{}".format(archive_name))
        run("mkdir -p /data/web_static/releases/{}/".format(
            archive_name[:-4]))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
            archive_name, archive_name[:-4]))
        run("rm /tmp/{}".format(archive_name))
        new_dir = "/data/web_static/releases/{}/".format(archive_name[:-4])
        run("mv /data/web_static/releases/{}/web_static/* {}".format(
                archive_name[:-4], new_dir))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_name[:-4]))
        run("rm -rf /data/web_static/current")
        ln_dir = "/data/web_static/current"
        run("ln -s /data/web_static/releases/{}/ {}".format(
             archive_name[:-4], ln_dir))
        return True
    except Exception:
        return False


def deploy():
    """Deploys content to the web server"""
    file_path = do_pack()
    if file_path is None:
        return False
    val = do_deploy(file_path)
    return val
