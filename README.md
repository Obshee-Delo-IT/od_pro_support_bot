# Obshee-Delo PRO support bot

# Install
<ul>
<li> <strong>Copy from git</strong>

```bash
cd py
git clone https://github.com/obshee-delo-ru/od_pro_support_bot.git
```

</li>

<li> <strong>Create virtual env on hosting: <a href="https://timeweb.com/ru/docs/virtualnyj-hosting/prilozheniya-i-frejmvorki/python-ustanovka-virtualenv/">timeweb</a></strong>

</li>

<li> <strong>Create virtual env Linux</strong>

```bash
cd py
python3 -m venv env
pip install -r req.txt
```

</li>
<li> <strong>Create virtual env Windows</strong>

```bash
cd py
python -m venv env
pip install -r req.txt
```

</li>

</ul>

# Start

<strong>Startup</strong>

```bash
python3 bot.py
```


<strong>Linux startup with resistant to terminal closure (like ssh disconnect)</strong>  
through nohup (resistent to input/output closure as well):
```bash
cd py
wget https://raw.githubusercontent.com/Obshee-Delo-IT/od_pro_support_bot/main/bot.py

source venv/bin/activate
pip install pyTelegramBotAPI==4.14.0
nohup python3 bot.py > od-pro-bot.out 2>&1 &
```

through disown:
```bash
env/Scripts/python bot.py & disown %1
#(jobs -l to check a worker not in session)
#ps aux to check worker
```
