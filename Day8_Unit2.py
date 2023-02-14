from slack_sdk import WebClient
from flask import Flask
from slackeventsapi import SlackEventAdapter
from slack_sdk.errors import SlackApiError
import random
import requests
import time

SLACK_TOKEN = "SLACK_TOKEN"
SIGNING_SECRET = "SIGNING_SECRET"

app = Flask(__name__)
slack_event_adapter = SlackEventAdapter(SIGNING_SECRET, '/slack/events', app)

client = WebClient(token=SLACK_TOKEN)

cat_images = [
    "https://cataas.com/cat",
    "https://thecatapi.com/api/images/get?format=src&type=gif",
    "https://thecatapi.com/api/images/get?format=src&type=jpg",
    "https://thecatapi.com/api/images/get?format=src&type=png"
]

@slack_event_adapter.on('message')
def message(payload):
    print(payload)
    event = payload.get('event', {})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')

    if text == "hi":
        client.chat_postMessage(channel=channel_id, text="Hello")

    if text == "cat":
        while True:
            try:
                cat_image_url = random.choice(cat_images)
                response = requests.get(cat_image_url)
                if response.status_code == 200:
                    client.files_upload(
                        file=response.content,
                        initial_comment='This is a sample Image',
                        channels=channel_id
                    )
                    print(f"Cat image sent to user {user_id}")
                else:
                    print(f"Failed to download cat image: {response.status_code}")
            except SlackApiError as e:
                assert e.response["ok"] is False
                assert e.response["error"]
                print(f"Got an error: {e.response['error']}")
            time.sleep(300)

if __name__ == "__main__":
    app.run(debug=True)
