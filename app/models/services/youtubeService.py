from apiclient.discovery import build

DEVELOPER_KEY = "AIzaSyCGDNtQf2lyE-905kYNj-z37ObM-NzV33s"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


class Youtube():
    def __init__(self):
        self.apiYoutube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                developerKey=DEVELOPER_KEY)

    def buscarListaVideos(self, termo):
        listaVideos = None
        listaVideosApi = self.apiYoutube.search().list(
            q=termo,
            part="id, snippet",
            maxResults=20,
            type='video',
        ).execute()
        listaVideos = []
        for infoVideo in listaVideosApi.get("items", []):
            listaVideos.append({"id": infoVideo['id']['videoId'], "titulo": infoVideo['snippet']
                                ['title'], "img": infoVideo['snippet']['thumbnails']['default']['url']})
        return listaVideos

    def buscarVideo(self, id):
        video = None
        try:
            video = self.apiYoutube.videos().list(
                part='snippet',
                id=id
            ).execute()
        except:
            print("Erro ao buscar vídeo")
        return video

    def  buscarComentarios(self, id):
        comentarios = []
        try:
            comentariosApi = self.apiYoutube.commentThreads().list(
                part='snippet',
                videoId=id,
                maxResults=100,
            ).execute()
            for infoComentario in comentariosApi.get("items", []):
                comentarios.append(infoComentario['snippet']['topLevelComment']['snippet']['textOriginal'])
        except:
            print("Erro ao buscar comentários do vídeo")
        return comentarios

    def retornarVideo(self, id):
        infoVideo = None
        try:
            video = self.buscarVideo(id)
            comentarios = self.buscarComentarios(id)
            infoVideo = {"informacoes": video, "comentarios": comentarios}
        except:
            print("Erro ao retornar informações do vídeo")
        return infoVideo
