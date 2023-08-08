import slack_sdk
from slack_sdk import WebClient
from slack_sdk.rtm_v2 import RTMClient

# instantiate WebClient
slack_token = 'xoxb-23072537313-5702482460518-9j1BvWA2PFJoISjz2QsiCwRz'
client = WebClient(token=slack_token)

@RTMClient.run_on(event='message')
def respond_to_message(**payload):
    data = payload['data']
    web_client = payload['web_client']
    if 'Hello' in data.get('text', []):
        channel_id = data['channel']
        thread_ts = data['ts']
        user = data['user']

        web_client.chat_postMessage(
            channel=channel_id,
            text=f"Hello <@{user}>!",
            thread_ts=thread_ts
        )

rtm_client = RTMClient(token=slack_token)
rtm_client.start()