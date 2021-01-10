# reddit-posts
The bot responsible for automatically sending new posts into #reddit-posts on Discord.

# Configuration
To setup the bot, update the following lines:
1. `client_id` and `client_secret` with your [Reddit API](https://www.reddit.com/prefs/apps/) information. 
2. `channel = bot.get_channel(0000000000000000)` with your Discord channel ID.
3. `bot.run("")` with your [Discord API](https://discord.com/developers/applications) token.

# Deployment
This bot is typically deployed using [pm2](https://pm2.keymetrics.io/) but can easily be deployed in a screen/tmux session. 
