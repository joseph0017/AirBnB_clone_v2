#!/usr/bin/python3
#Fabric script that generates a .tgz archive from the contents of
#the web_static folder of your AirBnB Clone repo, using the function do_pack

from fabric.api import local
from datetime import datetime

def do_pack():
    """Creates a tgz archive from the contents of the web_static folder"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = f"versions/web_static_{date}.tgz"
        local(f"tar -cvzf {file_name} web_static")
        return file_name
    except:
        return None
