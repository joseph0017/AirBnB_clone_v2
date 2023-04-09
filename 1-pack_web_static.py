#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """Creates a tgz archive from the contents of the web_static folder"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if os.path.isdir("versions") is False:
        local("mkdir -p  versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name
