import os, requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN') #TOKENはenvに保存

url = "https://discord.com/api/v8/users/@me/settings"

headers = {
            "host": "discord.com",
            "Authorization": DISCORD_TOKEN,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0", #UAはお好みで（サンプルはfirefox）
            "Content-Type": "application/json",
            "Accept": "*/*"
}
jsonData = {
        "status":"idle", #dnd, idle, online, invisibleから選んでくだしあ
        "custom_status":{
            "text":"Voidproer.", #ステータスをメッセージ
            "emoji_id":"1121243626928865301", #絵文字id
            "emoji_name":"earlydeveloper"
            }
}
response = requests.patch(url, headers=headers ,json=jsonData, verify=False) #sslエラーはめんどいから脳筋突破
