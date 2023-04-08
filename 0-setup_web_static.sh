#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/{releases,shared}
sudo mkdir /data/web_static/releases/test/
echo -e "<html>\n  <head></head>\n  <body>Just Testing Alx content.</body>\n</html>" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
CONFIG="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}"
sed -i "40i\ $CONFIG" /etc/nginx/sites-available/default
sudo service nginx restart
