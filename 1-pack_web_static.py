#!/usr/bin/python3
"""
 Fabric script that generates a .tgz archive from the contents of the
 web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local, env
from datetime import datetime

env.hosts = ['localhost']


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"versions/web_static_{timestamp}.tgz"
    local(f"tar -cvzf {filename} web_static")
    return filename
