#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

# install nginx if not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get -y update
	sudo apt-get -y install nginx
fi

# folders and files to be created
folders=(  "/data/web_static/releases/test/" "/data/web_static/shared/" )
files="/data/web_static/releases/test/index.html"

# check if folders already exist and create if non existent
mkdir -p ${folders[0]}
mkdir -p ${folders[1]}

# check if files exist and create if they don't exist
touch "$file"
echo "<h1>Testing My website</h1>" >> "$file"

# symbolic links
link_to="/data/web_static/releases/test/"
sym_link="/data/web_static/current"

# recreates a symbolic link and -f forces overwriting if another link exists
ln -sf "$link_to" "$sym_link"

# change ownership and group ownership to ubuntu and give privileges
sudo chown -R ubuntu:ubuntu /data/
sudo chown -R 755 /data/

# update the nginx configuration to serve content to hbnb_static
sudo sed -i '48i \\t location /hbnb_static/ {\n\talias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default
# restart nginx
sudo service nginx restart
