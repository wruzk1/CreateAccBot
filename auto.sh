screen -S AUTONUM -X kill
screen -S TOR9050 -X kill
fuser -k 9050/tcp
screen -d -m -S AUTONUM python3.8 bot.py
screen -d -m -S TOR9050 tor
