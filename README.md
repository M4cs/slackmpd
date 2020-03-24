# slackmpd
Rich Presence for mpd on Slack | Written in Python :snake:

<p align="center">
    <center><a align="center"><img src="https://pbs.twimg.com/media/ET0kZxjXkAAHpgk?format=png&name=900x900" height="450px"></a></center>
</p>

## Installation

- *Requires Python 3.6+*

Installation Steps for All Systems:

```
git clone git@github.com:M4cs/slackmpd.git
cd slackmpd/
pip install virtualenv
virtualenv .venv

# On Mac and Unix
source .venv/bin/activate
# On Windows
.venv\Scripts\activate.bat

pip install python-mpd2 slackclient

python -m slackmpd
```

Config is stored in `~/.config/slackmpd/config.json`

Default Config:

```json
{
    "mpd":{
        "host": "localhost",
        "port": 6600
    },
    "timeout": 10,
    "idletimeout": 30,
    "slack": {
        "workspaces": []
    },
    "formatting": "artist - song"
}
```

### Config Descriptions:

- **mpd.host -** The host name of your MPD client
- **mpd.port -** The port for MPD
- **timeout -** MPD Timeout (Default 10 Seconds)
- **idletimeout -** MPD Idletimeout (Default 30 Seconds)
- **slack.workspaces -** Array of xoxp ([Legacy Slack Docs](https://api.slack.com/legacy/custom-integrations/legacy-tokens) **These will only work for the next month or so. Ill look for a lookaround if people use this lol**) tokens
- **formatting -** Formatting of message. Accepts `%artist%, song, and album placeholders
