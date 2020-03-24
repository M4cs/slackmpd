import os, json

DEFAULT_CONFIG ={
    "mpd":{
        "host": "localhost",
        "port": 6600
    },
    "timeout": 10,
    "idletimeout": 30,
    "slack": {
        "workspaces": []
    },
    "formatting": "%artist% - %song%"
}

class Startup:

    def __init__(self, config_file=None):
        self.config_dir = os.path.realpath(os.path.expanduser("~") + "/.slackmpd")
        if not os.path.exists(self.config_dir):
            os.makedirs(self.config_dir)
        self.custom_config = False
        if not config_file:
            self.config_file = os.path.realpath(self.config_dir + "/config.json")
            if not os.path.exists(self.config_file):
                with open(self.config_file, "w+") as jf:
                    json.dump(DEFAULT_CONFIG, jf, indent=4)
        else:
            self.config_file = os.path.realpath(config_file)
            self.custom_config = True
    def parse_config(self):
        try:
            with open(self.config_file, "r+") as jf:
                config = json.load(jf)
                return config
        except FileNotFoundError:
            print("Couldn't find specified configuration file: " + self.config_file)
            exit(1)
    
    def get_config(self):
        return self.parse_config()