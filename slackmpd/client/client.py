from mpd import MPDClient
from slack import WebClient
from slack.errors import SlackApiError
from slackmpd.util import status

class Client:

    def __init__(self, config):
        self.config = config
        self.mpdclient = MPDClient()
        self.mpdclient.timeout = config.getTimeout()
        self.mpdclient.idletimeout = config.getIdleTimeout()
        host, port = config.getMpdCreds()
        self.mpdclient.connect(host, port)
        self.slackclients = {}
        for index, workspace in enumerate(config.getSlackWorkspaces()):
            webclient = WebClient(token=workspace)
            self.slackclients[index] = webclient
        for key, client in self.slackclients.items():
            try:
                client.channels_list()
            except SlackApiError:
                print("You seem to have a bad token! Please Check Your Config")
                exit(1)


    def setStatus(self):
        return status.build_status(self.config, self.mpdclient.currentsong())
