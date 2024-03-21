from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
load_dotenv ()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('SECRET')
playlist_id = os.environ.get('PLAYLIST')
user = os.environ.get('USER')

def get_token():
    auth = client_id+  ':' +client_secret
    auth_bytes = auth.encode('utf-8')
    autth_base64 =str(base64.b64encode(auth_bytes), 'utf-8')

    url= "https://accounts.spotify.com/api/token"
    headers= {
        'Authorization': 'Basic '+autth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'


    }
    data= {
        'grant_type': 'client_credentials'
    }
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result['access_token']
    return token



def get_auth_header(token):
    return {
        'Authorization': 'Bearer '+token
    }
    

def get_playlist(token,user_id):
    playlists= []
    url =f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers =get_auth_header(token)
    result = get(url, headers=headers)
    # json_result = json.loads(result.content)['items']
    for item in json.loads(result.content)['items']:
        playlists.append({
             item['name']
           
        })

    return playlists

token = get_token()

playlist = get_playlist(token,'creepy879')

for id,name in enumerate(playlist):
    print(name)





