#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/
sudo echo "Holberton School" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo chown -R "$USER":"$USER" /etc/nginx/
sudo printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    location /hbnb_static {
      alias /data/web_static/current/;
    }
    error_page 404 /404.html;
    location = /404.html {
      root /var/www/html;
    }
}" | sudo tee /etc/nginx/sites-available/default
sudo service nginx restart
