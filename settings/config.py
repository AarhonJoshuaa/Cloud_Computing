import os
ENV = "DEV" 
if ENV == "DEV1":
    from settings import keys
    telegram_key = keys.telegram_key
elif ENV == "DEV":
    import ast
    telegram_key = ast.literal_eval(os.environ["telegram_key"])
host = "0.0.0.0"
port = int(os.environ.get("PORT", 6000))