# orchest-coqui-tts
This repository demonstrates an Orchest pipeline that generates an audio fragment using the [coqui](https://github.com/coqui-ai/TTS) TTS engine and sends it as a message on Slack

## Environment variables
If you want to send this to your actual Slack channel you need a bot with chat:read/write and file:read/write permissions and set the `SLACK_BOT_TOKEN` environment variable.

Make sure you add the bot the desired channel. The Slack channel can be overwritten by specifying the `SLACK_CHANNEL` environment variable.

### Pipeline

![Pipeline visualization](https://pviz.orchest.io/?pipeline=https://github.com/ricklamers/orchest-coqui-tts/blob/main/main.orchest)

