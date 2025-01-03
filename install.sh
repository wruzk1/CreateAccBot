apt update
apt install -y redis-server screen python3.8 python3.8-dev tor zip torsocks python3.8-distutils
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.8 get-pip.py
python3.8 -m pip install -U telethon
python3.8 -m pip install pyrogram
python3.8 -m pip install tgcrypto
python3.8 -m pip install redis
python3.8 -m pip install stem
read tokens
redis-cli sadd TOKEN $tokens
sudo sed -i 's/#AllowInbound 1/AllowInbound 1/g' /etc/tor/torsocks.conf
sudo sed -i 's/#AllowOutboundLocalhost 1/AllowOutboundLocalhost 1/g' /etc/tor/torsocks.conf