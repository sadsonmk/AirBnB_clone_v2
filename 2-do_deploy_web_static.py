#!/usr/bin/python3
"""a Fabric script (based on the file 1-pack_web_static.py)
    that distributes an archive to your web servers,
    using the function do_deploy
"""

import os
from fabric.api import run, env, put

env.hosts = ['18.209.225.36', '52.87.234.219']


def do_deploy(archive_path):
    """distributes an archive to webservers"""

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        ext_filename = archive_path.split('/')[-1]
        filename = ext_filename.split('.')[0]

        run(f'mkdir -p /data/web_static/releases/{filename}')
        run(f'tar -xzf /tmp/{ext_filename} -C
            /data/web_static/releases/{filename}')
        run(f'rm /tmp/{ext_filename}')

        run(f'mv /data/web_static/releases/{filename}/web_static/*
            /data/web_static/releases/{filename}/')
        run(f'rm -rf /data/web_static/releases/{filename}/web_static')
        run('rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{filename}/
            /data/web_static/current')
        return True
    except:
        return False
