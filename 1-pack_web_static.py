#!/usr/bin/python3
"""This module defines a function that generates an archive of contens of
web_static folder"""


from fabric.api import local, env
from datetime import datetime

env.hosts = ['localhost']


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder
    """
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -cvzf {} web_static".format(filename))
    return filename
