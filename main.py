import random
import spotipy
import sys
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = ''
CLIENT_SECRET = ''

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

def get_random_song(playlist_id):
    try:
        tracks = sp.playlist_tracks(playlist_id)['items']

        if not tracks:
            return "플레이리스트에서 노래를 찾을 수 없습니다."

        random_track = random.choice(tracks)['track']

        return (f"🎵 랜덤으로 추천된 노래 🎵\n"
                f"제목: {random_track['name']}\n"
                f"아티스트: {', '.join(artist['name'] for artist in random_track['artists'])}\n"
                f"앨범: {random_track['album']['name']}\n"
                f"[노래 듣기]({random_track['external_urls']['spotify']})")

    except Exception as e:
        return f"API 요청 중 오류가 발생했습니다: {e}"

def music_info():
    while True:
        song_name = input("검색하고 싶으신 노래 제목을 입력하세요 (종료: exit): ").strip()
        if song_name.lower() == "exit":
            print("프로그램 종료")
            break

        results = sp.search(q=song_name, limit=1, type="track")
        if results['tracks']['items']:
            track = results['tracks']['items'][0]
            print("\n[노래 정보]")
            print(f"제목: {track['name']}")
            print(f"아티스트: {', '.join(artist['name'] for artist in track['artists'])}")
            print(f"앨범: {track['album']['name']}")
            print(f"발매일: {track['album']['release_date']}")
            print(f"미리 듣기: {track['preview_url'] if track['preview_url'] else '미리 듣기 불가'}")
            print(f"Spotify 링크: {track['external_urls']['spotify']}")
        else:
            print("❌ 해당 노래를 찾을 수 없습니다.")
def playlist_info():
    while True:
        playlist_name = input("플레이리스트 코드를 입력하세요.(종료 : exit): " ).strip()
        if playlist_name.lower() =="exit":
            print("프로그램 종료")
            break
    

def main():
    Command_list = ["PlaylistRandomRCMD", "MusicInfo", "Playlist_Info"]
    Command_name = input("명령어 입력 (PlaylistRandomRCMD / MusicInfo / PlaylistInfo): ").strip()

    if Command_name not in Command_list:
        print("명령어를 찾을 수 없습니다.")
        sys.exit()

    if Command_name == "PlaylistRandomRCMD":
        playlist_id = input("플레이리스트 ID를 입력하세요: ").strip()
        song_info = get_random_song(playlist_id)
        print(song_info)
    elif Command_name == "MusicInfo":
        music_info()
    elif Command_name == "PlaylistInfo":
        playlist_info()
        
        

if __name__ == '__main__':
    main()
