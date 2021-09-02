#!/bin/bash

# Install any dependencies you have in this shell script.
pip install boto3 requests psycopg2-binary pandas sqlalchemy slack_sdk discord nest_asyncio
pip install TTS --ignore-installed

# Pre-download model
tts --text "Hello" --model_name 'tts_models/en/vctk/vits' --out_path "/tmp/test.wav" --speaker_idx p228