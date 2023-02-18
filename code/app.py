import os
from slack_bolt import App
from revChatGPT.V1 import Chatbot
import json

# Load the configs
with open("config.json") as f:
    config = json.load(f)

# Initalize the ChatGPT chatbot
# You can use other authentication methods indicated in https://github.com/acheong08/ChatGPT
chatbot = Chatbot(
    config={
        "access_token": config["chatgpt_access_token"],
        "paid": config["chatgpt_paid"],
    }
)

# Initialize Slack app with bot token and signing secret
# See https://slack.dev/bolt-python/tutorial/getting-started for tutorial
app = App(
    token=config["slack_bot_token"], signing_secret=config["slack_signing_secret"]
)

# Handle mentions
@app.event("app_mention")
def handle_mention(say, body):
    user_name = f"<@{body['event']['user']}>"
    text = body["event"]["text"]

    for data in chatbot.ask(text):
        response = data["message"]
    say(f"{user_name} {response}")


# Start your app
if __name__ == "__main__":
    app.start(port=config["port"])
