from app.models.util import get_most_used_words

class LearningObject():
    def __init__(self, video):
        self.geral = {
            "id": video['informacoes']['items'][0]['id'],
            "titulo": video['informacoes']['items'][0]['snippet']['title'],
            "idioma": "English",
            "descricao": video['informacoes']['items'][0]['snippet']['description'],
            "palavras_chave": None, #get_most_used_words(video, 5),
            "cobertura": None,
            "estrutura": None,
            "nivel_de_agregacao": None,
        }
        self.ciclo_de_vida = {
            "versao": None,
            "status": None,
            "contribuinte": {
                "entidade": None,
                "data": None,
                "papel": None
            }
        }
        self.meta_metadados = {
            "identificador": {
                "catalogo": None,
                "entrada": None
            },
            "contribuinte": {
                "entidade": "Youtube",
                "data": None,
                "papel": None,
            },
            "esquema_de_metadados": "IEEE LOM",
            "idioma": "Português"
        }
        self.metadados_tecnicos = {
            "formato": "text/html",
            "tamanho": None, #len(list(video.content)),
            "localizacao": None,
            "requisitos": None,
            "observacoes_de_Instalacoes": None,
            "outros_requisitos_de_sistema": None,
            "duracao": None
        }
        self.aspectos_educacionais = {
            "tipo_de_iteratividade": "Expositiva",
            "tipo_de_recurso_de_aprendizado": "Texto narrativo",
            "nivel_de_interatividade": "Pequena",
            "densidade_semantica": "Alta",
            "usuario_final": "Público geral",
            "contexto_de_aprendizagem": None,
            "idade_recomendada": "Adulto",
            "grau_de_dificuldade": None,
            "tempo_de_aprendizado": None,
            "descricao": None,
            "linguagem": "Português"
        }
        self.direitos = {
            "custo": 0.0,
            "direitos_autorais": "Domínio público",
            "descricao": None
        }
        self.relacoes = {
            "genero": "Fontes Externas",
            "recurso": {
                "referencias": None,
                "links_externos": None
            }
        }
        self.classificacao = {
            "finalidade": None,
            "diretorio": None,
            "descricao": None,
            "palavra_chave": None
        }
        self.conteudo = {
            "data": None,
            "entidade": None,
            "imagens": None,
            "comentarios": None,
        }
    

    def get_as_json(self):
        return self.__dict__
