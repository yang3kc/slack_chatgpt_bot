# [This repo has been deprecated]

You can now use the [offical ChatGPT API](https://openai.com/blog/introducing-chatgpt-and-whisper-apis) to build bots.
Moreover, Slack has [announced](https://www.salesforce.com/news/stories/chatgpt-app-for-slack/) the offical ChatGPT app.

# A simple ChatGPT bot for Slack

![slack_bot](https://user-images.githubusercontent.com/31357713/219899609-fbf0ddb4-e52e-4369-b5c1-8a60d420e0d5.gif)

# What you need

## Logistics

- You will need a server with Internet access to host the backend of the bot. I'm using a Ubuntu machine.
- You will need a ChatGPT account.
- You will need to create a Slack app with at least the permission to write to the channels (see https://api.slack.com/authentication/basics for instructions)

## Dependencies

- [Reverse Engineered ChatGPT API](https://github.com/acheong08/ChatGPT): to interact with ChatGPT
- [slack_bolt](https://slack.dev/bolt-python/tutorial/getting-started): to interact with Slack

# How to run the bot

Go to `code` folder

```sh
cp config_template.json config.json
```

Add your credentials and configuration to it. Then you can fun the backend with

```sh
python app.py
```
