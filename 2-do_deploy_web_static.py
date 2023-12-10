#!/usr/bin/python3
"""
Its a python script that creates and distributes an
archive to your web servers, using the function deploy
"""

from fabric.api import put, env, run
import os

env.hosts = ['18.209.225.36', '52.87.234.219']


def do_deploy(archive_path):
    """distributes files(archive) to my webservers"""

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        ext_file = archive_path.split("/")[-1]
        filename = ext_file.split(".")[0]
        run('mkdir -p /data/web_static/releases/{}'.format(filename))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format
            (ext_file, filename))
        run('rm /tmp/{}'.format(ext_file))
        run('mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/'.format(filename, filename))
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{} /data/web_static/current'
            .format(filename))

        return True

    except Exception:
        return False
