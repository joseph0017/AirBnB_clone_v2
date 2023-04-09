#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers, using the function do_deploy
"""
from datetime import datetime
from fabric.api import env, local, run, put
import os

env.hosts = ['54.237.35.82', '18.209.224.87']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    distributes an archive to your web servers,
    using the function do_deploy
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        filename = archive_path.split("/")[-1]
        foldername = ("/data/web_static/releases/" + filename.split(".")[0])
        run("mkdir -p {}".format(foldername))
        run("tar -xzf /tmp/{} -C {}".format(filename, foldername))
        run("rm /tmp/{}".format(filename))
        run("mv {}/web_static/* {}/".format(foldername, foldername))
        run("rm -rf {}/web_static".format(foldername))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(foldername))
        return True
    except:
        return False
