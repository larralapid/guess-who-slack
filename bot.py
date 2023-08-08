from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token="xoxb-23072537313-5702482460518-9j1BvWA2PFJoISjz2QsiCwRz", signing_secret="36dc3726212897abf360add7dda0d67e")

@app.command("/guesswho")
def handle_guesswho(ack, command, client):
    # Acknowledge the command request
    ack()
    
    # Process the command
    response_text = "You initiated a Guess Who game!!"
    
    # Send a response
    client.chat_postEphemeral(
        channel=command["channel_id"],
        user=command["user_id"],
        text=response_text
    )
if __name__ == "__main__":
    SocketModeHandler(app, "xapp-1-A05LV0NDQN6-5732789533200-716969f0baadb571500ed939e54b50038b1f8288538409eabb7c44bfde3e06d2
").start()
