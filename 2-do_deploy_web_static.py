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
    file_name = os.path.basename(archive_path)
    path_release = splitext(f"/data/web_static/releases/{file_name}")[0]
    path_current = '/data/web_static/current'
    try:
        if os.path.exists(archive_path) is None:
            return False
        put(archive_path, f"/tmp/{file_name}")
        run(f"mkdir -p {path_release}")
        run(f"tar -xzf /tmp/{file_name} -C {path_release}")
        run(f"rm /tmp/{file_name}")
        run(f"mv {path_release}/web_static/* {path_release}")
        run(f"m -rf {path_release}/web_static")
        run(f"rm -rf {path_current}")
        run(f"ln -s {path_release} {path_current}")
        print("yaaay!! New version deployed!")
        return True
    except Exception:
        return False
