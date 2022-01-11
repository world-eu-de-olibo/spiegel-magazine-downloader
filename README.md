# Note: The downloader works only if you have a valid subscription from www.spiegel.de

sudo su root

apt-get update && apt-get upgrade && apt-get dist-upgrade

apt-get install npm python3 python3-pip python3.8 python3-pip libpython3.8-dev libpython3-all-dev git

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

apt install ./google-chrome-stable_current_amd64.deb

rm ./google-chrome-stable_current_amd64.deb

exit

python3 -m pip install --upgrade pip

pip install webdriver-manager

pip install -U selenium

cd /home/YOURUSERNAME # change username

git clone https://github.com/eu-de-olibo/spiegel-magazine-downloader

cd spiegel-magazine-downloader

vi get-all-spiegel-magazines.py # change username and password

python3 get-all-spiegel-magazines.py
