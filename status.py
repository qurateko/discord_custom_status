import sys, os, time, requests, random, requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
#DISCORD_TOKENはenvファイルに記載
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
#v9はよくわかんないからv8のapiを叩く
url = "https://discord.com/api/v8/users/@me/settings"

headers = {
            "Host": "discord.com",
            "Authorization": DISCORD_TOKEN,
            # User Agent is your choice.  
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
            "Content-Type": "application/json",
            "Accept": "*/*"
}
jsonData = {
        "custom_status":
       #ステータスメッセージ   
        {"text":"Voidproer.",
         #ステータスに設定する絵文字
         "emoji_id":"1121243626928865301",
         "emoji_name":"earlydeveloper"}
}
response = requests.patch(url, headers=headers ,json=jsonData, verify=False) #sslのエラーは脳筋解決
