#!/bin/bash

# Install any dependencies you have in this shell script.

sudo apt-get update && sudo apt-get install dnsutils -y

pip install boto3 requests psycopg2-binary pandas sqlalchemy slack_sdk
pip install TTS --ignore-installed
pip install discord

# Pre-download model
tts --text "Hello" --model_name 'tts_models/en/vctk/vits' --out_path "/tmp/test.wav" --speaker_idx p228