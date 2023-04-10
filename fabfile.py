#!/usr/bin/python3
"""
function that generates an archive of contents of
web_static folder
"""


from fabric.api import local, env
from datetime import datetime
import os

env.hosts = ['54.237.35.82', '18.209.224.87']
env.user = 'ubuntu'
env.key_file_name = '~/.ssh/id_rsa'


def do_pack():
    """Creates a tgz archive from the contents of the web_static folder"""
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    if os.path.isdir("versions") is False:
        local("mkdir -p  versions")
    file_name = "versions/web_static_{}.tgz".format(date)
    local("tar -cvzf {} web_static".format(file_name))
    return file_name

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

def deploy():
    """Distributes content to the web server"""
    file_path = do_pack()
    if file_path is None:
        return False
    return do_deploy(file_path)
