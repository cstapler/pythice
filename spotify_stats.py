import sys
import os
import spotipy
import spotipy.util as util

scope = 'user-top-read'
client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri="http://localhost:8888/callback")

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks()
    for item in results['items']:
        print(item['name'] + ' - ' + item['artists'][0]['name'])
else:
    print("Can't get token for", username)
