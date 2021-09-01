import os
import uuid
import shlex
import subprocess
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


channel = "#pipeline-exploration"


def generate_audio_file(text, path, speaker="p228"):
    command = "tts --text %s --model_name 'tts_models/en/vctk/vits' --out_path %s --speaker_idx %s" % (shlex.quote(text), shlex.quote(path), speaker)
    print(command)
    print(f"{subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True).decode()}")

    
def send_slack_message(message):
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    try:
        response = client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")

        
def send_slack_file(file_path, title):
    
    client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])
    
    try:
        client.files_upload(
            channels=channel,
            file=file_path,
            title=title
        )
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
        print(f"Got an error: {e.response['error']}")