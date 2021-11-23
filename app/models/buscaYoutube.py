from apiclient.discovery import build

DEVELOPER_KEY = "key"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Busca():
    def __init__(self):
        self.youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
        developerKey=DEVELOPER_KEY)

    def videos(self, termo):
        search_response = self.youtube.search().list(
        q=termo,
        part="id, snippet",
        maxResults=20,
        type='video',
        ).execute()

        videos = []

        for search_result in search_response.get("items", []):
                videos.append({"id": search_result['id']['videoId'], "titulo": search_result['snippet']['title']})
       
        return(videos)
            
    def videoPorId(self, id):
        try:
            video = self.youtube.videos().list(
            part='snippet,localizations',
            id=id
            ).execute()
            return video
        except:
            print("Erro ao acessar API do youtube")

