from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyBJPJzM0oyrZLthEiptqztpXs8JhzpIATI"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

class Youtube():
    def __init__(self):
        self.apiYoutube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, 
        developerKey=DEVELOPER_KEY)

    def buscarListaVideos(self, termo):
        try:
            listaVideosApi = self.apiYoutube.search().list(
            q=termo,
            part="id, snippet",
            maxResults=20,
            type='video',
            ).execute()
            listaVideos = []
            for infoVideo in listaVideosApi.get("items", []):
                    listaVideos.append({"id": infoVideo['id']['videoId'], "titulo": infoVideo['snippet']['title']})
        except:
            print("Erro ao acessar API do youtube")
        return listaVideos if listaVideos else None
            
    def buscarVideo(self, id):
        infoVideo = None
        try:
            infoVideo = self.apiYoutube.videos().list(
            part='snippet',
            id=id
            ).execute()
        except:
            print("Erro ao acessar API do youtube 1")
        return infoVideo.get("items") if infoVideo else infoVideo

    def buscarComentarios(self, id):
        # comentarios = None
        # try:
        infoComentariosApi = self.apiYoutube.commentThreads().list(
        part='snippet',
        videoId=id
        ).execute()
        comentarios = []
        for infoComentario in infoComentariosApi.get("items", []):
            comentarios.append(infoComentario['snippet']['topLevelComment']['snippet'])
        # except:
            # print("Erro ao acessar API do youtube 2")
        return comentarios

    def retornarVideo(self, id):
        # infoVideo = None
        # try:
        infoBasicas = self.buscarVideo(id)
        comentarios = self.buscarComentarios(id)
        infoVideo = {"informacoes": infoBasicas, "comentarios": comentarios}
        # except:
            # print("Erro ao acessar API do youtube 3")
        return infoVideo

    

