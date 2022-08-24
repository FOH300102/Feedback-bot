# @KEK_Projects


import pyromod.listen
from pyrogram import Client
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

app = Client(
    "bot",
    api_id=env.API_ID,
    api_hash=env.API_HASH,
    bot_token=env.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="database"),
)

if __name__ == "__main__":
    print("Starting Private Chat Bot...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} started successfully !")
    idle()
    app.stop()
    print("Bot stopped. Bye !")
