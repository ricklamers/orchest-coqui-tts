import os
import uuid
import shlex
import subprocess
import asyncio
import discord
import nest_asyncio
import sys

from multiprocessing import Process

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

channel = os.getenv("SLACK_CHANNEL", "#general")

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
        

def _send_discord_file(file_path, title):
    
    discord_channel = int(os.getenv("DISCORD_CHANNEL_ID", "0"))
    client = discord.Client()

    async def my_background_task():
        await client.wait_until_ready()
        channel = client.get_channel(id=discord_channel) # replace with channel_id
        await channel.send(title, file=discord.File(file_path))
        await client.close()
    
    client.loop.create_task(my_background_task())
    
    try:
        client.run(os.environ['DISCORD_BOT_TOKEN'])
    except Exception as e:
        pass


def send_discord_file(file_path, title):
    
    nest_asyncio.apply()
    
    p = Process(target=_send_discord_file, args=(file_path, title))
    p.start()
    p.join()
