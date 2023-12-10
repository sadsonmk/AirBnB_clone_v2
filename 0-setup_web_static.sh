#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

# install nginx if not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

# check if folders already exist and create if non existent
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# check if files exist and create if they don't exist
touch /data/web_static/releases/test/index.html
echo "<h1>Testing My website</h1>" > /data/web_static/releases/test/index.html

# recreates a symbolic link and -f forces overwriting if another link exists
ln -sf /data/web_static/releases/test/ /data/web_static/current

# change ownership and group ownership to ubuntu and give privileges
sudo chown -R ubuntu:ubuntu /data/
sudo chown -R 755 /data/
# update the nginx configuration to serve content to hbnb_static
sudo sed -i '48i \\t location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default
# restart nginx
sudo service nginx restart
