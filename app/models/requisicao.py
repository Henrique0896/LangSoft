from apiclient.discovery import build

DEVELOPER_KEY = "chave"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Requisicao():
    def youtube_search(self, opcoes):
       
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

        search_response = youtube.search().list(
            q=opcoes['termo'],
            part=opcoes['propriedades'],
            maxResults=opcoes['maxresultados'],
            type=opcoes['tipo'],
        ).execute()

        videos = []

        for search_result in search_response.get("items", []):
                videos.append(search_result['snippet']['title'])
       
        return(videos)

    def teste(self):
        opcoes = {
            "termo": "E o galo?",
            "propriedades" : "id, snippet",
            "maxresultados": 20,
            "tipo": "video"
        }
       
        try:
            return self.youtube_search(opcoes)
        except:
            print("Erro ao acessar api")
