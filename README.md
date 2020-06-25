# Section Check for Bilkent University

### Installation
1) You should have pyglet package to hear the sound.

```
pip install pyglet
```
2) Move a wav file named siren.wav to same directory with python file.

3) Run main.py
```
python main.py
```

### Optional Discord Alerts
1) Install discord_webhook

2) Pass webhook url in main as:
```sectioncheck.courseCrawlerHandler(depts, courseCodes, sections, semester, year, webhookurl="your_url")```

3) Set webhookurl in main to your server's bot's url

Optional: You can make your bot ping you if you set your pingmsg to your mention id.(eg. <@140408733719138560> to find this look at [this](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID))
```sectioncheck.courseCrawlerHandler(depts, courseCodes, sections, semester, year, webhookurl="your_url", webhookmsg="<@140408733719138560>")```

### Example Config
```
fall
TUR-101
MATH-102
EEE-102-1,2,3
```

### Usage
Setup config.txt file.

Start main.py and just wait for a siren.

### Developing
You can use your own script to use the sectioncheck package.

Feel free to contribute and fork.

### Warning
Do not decrease sleep time.


