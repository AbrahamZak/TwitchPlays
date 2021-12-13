# TwitchPlays
Twitch plays app for accepting user input in twitch chat and executing it in game

## Environment variables
token - Oauth token from https://twitchapps.com/tmi/


## Run
Simply run TwitchPlays.py after establishing your environment variable token.

## Change acceptable key inputs / mappings
In KeyProcessor.py:

To change acceptable inputs update the keys variable in the process_key function

To change mappings update the key_mappings dictionary in the press_key function