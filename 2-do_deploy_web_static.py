#!/usr/bin/python3

from datetime import datetime
from fabric.api import env, local, run, put
import os

env.hosts = ['100.26.17.152', '54.89.109.11']
env.user = 'ubuntu'
env.key_filename = '~/id_rsa'


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
        run("mv /data/web_static/releases/{}/web_static/* {new_dir}".format(
                archive_name[:-4], archive_name[:-4]))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_name[:-4]))
        run("rm -rf /data/web_static/current")
        ln_dir = "/data/web_static/current"
        run("ln -s /data/web_static/releases/{}/ {}".format(
            ln_dir, archive_name[:-4]))
        return True
    except:
        return False
