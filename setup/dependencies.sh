echo "installing dependencies for b3na"

echo "isntalling python-dev"
sudo apt install -y python-dev

echo "installing pip"
sudo apt install -y python-pip

echo "installing arp-scan"
sudo apt install -y arp-scan

echo "installing pymongo"
sudo pip install pymongo

# echo "installing firebase"
# sudo pip install python-firebase

echo "installing pyserial"
sudo pip install pyserial

echo "installing httplib2"
sudo pip install httplib2

echo "installing google library for python"
sudo pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

echo "install pushbullet library"
sudo pip install pushbullet.py

echo "installing Philips HUE library"
sudo pip install qhue

echo "installing bottle server"
sudo pip install bottle

echo "installing schedule library"
sudo pip install schedule

echo "installing config parser"
sudo pip install ConfigParser

echo "installing psutil"
sudo pip install psutil

# trying flask framework for webapp
echo "installing flask"
sudo pip install flask

echo "installing Flask-WTF to handle web forms in flask"
sudo pip install flask-wtf

echo "installing flask SQLAlchemy to handle ORMs for SQL DBs"
sudo pip install flask-sqlalchemy

echo "installing falsk-migrate to handle DB migrations"
sudo pip install flask-migrate

echo "installing flask-login extension"
sudo pip install flask-login

echo "installing flask-bootstrap extension"
sudo pip install flask-bootstrap

echo "installing python-mysqldb"
apt-get install python-mysqldb

echo "installing Spotipy"
sudo pip install spotipy

echo "installing pychromecast"
sudo pip install pychromecast

echo "installing git"
sudo apt install -y git-all

echo "installing mplayer"
sudo apt install -y mplayer

echo "installing pico2wave"
sudo apt install -y libttspico-utils

echo "installing apache"
sudo apt install -y apache2

echo "done with the dependencies"
