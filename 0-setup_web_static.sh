#!/usr/bin/env bash
# This script sets up web servers for deployment of web_static
apt-get install -y nginx
mkdir -p /data/web_static/{releases,shared}
mkdir /data/web_static/releases/test/
echo -e "<html>\n  <head></head>\n  <body>This is a simple content.</body>\n</html>" > /data/web_static/releases/test/index.html
rm -f /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
CONFIG="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}"
sed -i "40i\ $CONFIG" /etc/nginx/sites-available/default
service nginx restart
