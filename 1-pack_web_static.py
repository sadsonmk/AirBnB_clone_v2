#!/usr/bin/python3
"""a Fabric script that generates a .tgz archive
    from the contents of the web_static folder of
    your AirBnB Clone repo, using the function do_pack
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of web_static"""
    local('mkdir -p versions')

    now = datetime.now()
    time_stamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{time_stamp}.tgz"

    archive_file = f"tar -cvzf {archive_name} web_static"

    archive_tar_file = local(archive_file)

    if archive_tar_file.succeeded:
        return archive_name
    return None
