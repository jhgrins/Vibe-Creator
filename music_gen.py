import sys
import spotipy
import spotipy.util as util
import pandas as pd 

#scope = 'user-library-read'
sc = 'user-top-read'

username = input("Enter username:")

token = util.prompt_for_user_token(username=username,scope=sc,client_id='33ebd71536d94caebcf54970eaf4191a',
                                  client_secret='87c219c0663d414388f96a6b7da7ee11', redirect_uri='http://localhost/')
								  
sp = spotipy.Spotify(auth=token)

user_data = {}
results = sp.current_user_top_tracks()
songs = []
ids = []
count = 0
print(username + "'s Top 20 songs")
print("----------------------------------")
for track in results['items']:
    count += 1
    songs.append(track)
    ids.append(track['id'])
    print(str(count) + '. ' + track['name'] + ' - ' + track['artists'][0]['name'])
    
features = sp.audio_features(ids)

for item in features:
    item.update( {"user": username})
user = pd.DataFrame(features)