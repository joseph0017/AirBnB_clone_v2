#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of
#the web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local
from datetime import datetime

def do_pack():
    """Creates a tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name
