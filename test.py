from dotenv import load_dotenv
import os
import base64
from requests import post,get
import json
load_dotenv ()

client_id = os.environ.get('CLIENT_ID')
client_secret = os.environ.get('SECRET')

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
    
def search (token,artist_name):
    url='https://api.spotify.com/v1/search'
    headers =get_auth_header(token)
    query = f'?q={artist_name}&type=artist&limit=1'


    query_url= url +query
    result =get(query_url,headers=headers)
    json_result = json.loads(result.content)['artists']['items']
    if len(json_result)==0:
        print('no restuls')
        return None
    return json_result[0]

    
def song (token, artist_id):
    url=f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US'
    headers =get_auth_header(token)
    result =get(url,headers=headers)
    json_result = json.loads(result.content)['tracks']
    return json_result
token = get_token()
result =search(token, 'KSI')


artist_id= result['id']

songs = song(token, artist_id)

for idx ,song in enumerate(songs):
    print(f"{idx+1} - {song['name']}")