# NexaevTG_bot

# Install 

<ul>
<li> <strong>Copy from git</strong>

```bash
git clone https://github.com/Jexelus/NexaevTG_bot
```

</li>

<li> <strong>Create virtual env Linux</strong>

```bash
cd NexaevTG_bot
python3 -m venv env
pip install -r req.txt
```

</li>
<li> <strong>Create virtual env Windows</strong>

```bash
cd NexaevTG_bot
python -m venv env
pip install -r req.txt
```

</li>

</ul>

# Start

<li> <strong>Startup Linux</strong>

```bash
env/bin/python bot.py
```

</li>
<li> <strong>Create virtual env Windows</strong>

```bash
env/Scripts/python bot.py
```

</li>

# Additional information
<strong>Linux startup with resistant to terminal closure (like ssh disconnect)</strong>

```bash
env/Scripts/python bot.py &
disown %1 #(jobs -l to check a worker not in session)
#ps aux to check worker
```
<strong>Linux demon script</strong>
```bat
[Unit]
Description=TGN_bot
After=network.target
[Service]
Type=simple
WorkingDirectory=<Path to rep>
ExecStart=<Path to env/bin/python> <Path to bot.py>
Restart=on-failure
RestartSec=5s
[Install]
WantedBy=multi-user.target
```
<strong>Start demon command</strong>
```bash
sudo systemd reload
sudo systemd start <name demon>
#check status sudo systemd status <name demon>
```
