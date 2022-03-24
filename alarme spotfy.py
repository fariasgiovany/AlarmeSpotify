import string

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import random
import time
import os



pl_id = 'playlist' #Nome da playlist que será usada como base
offset = 0
lista=[]

#conectando conta no spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="ID", #Id do Spotify de DEV
                                                client_secret="secret",#palavra senha do Spotify de DEV
                                                redirect_uri="http://localhost/", #Confirmação de login
                                                scope='playlist-modify-public,user-library-read, playlist-modify-private' )) #Objeto de autorização spotify
while True:
    offset = 0
    #Fazendo coleta de musicas da playslist base
    while True:

        response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total',
                                 additional_types=['track'])

        if len(response['items']) == 0:
            break

        print(response['items'])
        musicas=response['items']


        offset = len(response['items'])
        print(offset, "/", response['total'])

    #escolhendo música leatória
    i=random.randint(0,offset-1)
    print(musicas[i]["track"]["id"],i)
    mus2=musicas[i]["track"]["id"]
    print (mus2)

    #apagando os dados antigos da playlist de despertador
    playlist_id2="playlist 2" #playlist de destino da musica

    offset = 0
    response = sp.playlist_items(playlist_id2,
                                offset=offset,
                                fields='items.track.id,total',
                                additional_types=['track'])



    print(response['items'])
    offset = offset + len(response['items'])

    print(offset, "/", response['total'])
    teste=response['items']
    print (teste)
    mus=teste[0]["track"]["id"]
    print (mus)
    results = sp.playlist_remove_specific_occurrences_of_items(playlist_id2,[{"uri":mus,"positions":[0]}], snapshot_id=None)

    sp.user_playlist_add_tracks("farias.giovany",playlist_id2,[mus2])

    time.sleep(86400)


