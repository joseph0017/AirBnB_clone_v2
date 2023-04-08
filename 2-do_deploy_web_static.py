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
    serves an archive to web servers
    """
    if not os.path.exists(archive_path):
        return False
    try:
        archive_name = os.path.basename(archive_path)
        put(archive_path, f"/tmp/{archive_name}")
        run(f"mkdir -p /data/web_static/releases/{archive_name[:-4]}/")
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
