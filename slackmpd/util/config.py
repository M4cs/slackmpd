class Config:

    def __init__(self, config):
        if config.get('mpd'):
            if config['mpd'].get('host'):
                self.host = config['mpd']['host']
            else:
                self.host = "localhost"
                print("Missing host in config. Defaulting to localhost!")
            if config['mpd'].get('port'):
                self.port = config['mpd']['port']
            else:
                self.port = 6600
                print("Missing port in config. Defaulting to 6600")
        else:
            print("Missing MPD Config. Defaulting to localhost:6600")
        if config.get('timeout'):
            self.timeout = config['timeout']
        else:
            print("Missing timeout in config. Defaulting to 10 seconds")
            self.timeout = 10
        if config.get("idletimeout"):
            self.idletimeout = config['idletimeout']
        else:
            print("Missing idletimeout in config. Defaulting to None")
            self.idletimeout = None
        if config.get("slack"):
            if config['slack'].get("workspaces"):
                if not len(config['slack']['workspaces']) >= 1:
                    print("Missing workspace tokens for Slack! Exiting...")
                    exit(1)
                else:
                    self.workspaces = config['slack']['workspaces']
            else:
                print("Missing Slack configuration! Exiting...")
                exit(1)
        else:
            print("Missing Slack configuration! Exiting...")
            exit(1)
        if config.get("formatting"):
            self.formatting = config['formatting']
            print(self.formatting)
        else:
            self.formatting = "%artist% - %song%"

    def getMpdCreds(self):
        return self.host, self.port

    def getSlackWorkspaces(self):
        return self.workspaces

    def getTimeout(self):
        return self.timeout
    
    def getIdleTimeout(self):
        return self.idletimeout

    def getFormatting(self):
        return self.formatting