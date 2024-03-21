#!/usr/bin/env bash
#The script sets up web servers for deployment of my `web_static`.
#The script goes ahead to set up the necessary environment and configuartions.

if ! dpkg -l | grep -q nginx; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi 

sudo mkdir /data/web_static/releases/test/ /data/web_static/shared/

echo "<html>
    <head>
        <title>Test Page</title>
    </head>
    <body>
        <h1>This is a test page for web_static deployment</h1>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/we_static/currrent

sudo chown -R ubuntu:ubuntu /data
sudo sed -i '/^\s*server_name _;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service nginx restart
