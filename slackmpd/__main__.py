from slackmpd.util import Startup, Config
from slackmpd.client import Client
import time

def main():
    startup = Startup()
    configObj = startup.get_config()
    config = Config(configObj)
    client =  Client(config)
    while True:
        status = client.setStatus()
        print(status)
        for index, c in client.slackclients.items():
            c.api_call(
                api_method="users.profile.set",
                json={"profile": {
                    "status_text": status,
                    "status_emoji": ":musical_note:",
                    "status_expiration": 0
                }}
            )
        time.sleep(10)
if __name__ == "__main__":
    main()