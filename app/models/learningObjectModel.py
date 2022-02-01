class LearningObject(object):
    def __init__(self, video):
        self.geral = {
            "identificador": {
                "catalogo": "URI", 
                "entrada":"https://www.youtube.com/watch?v="+video['informacoes']['items'][0]['id']
            },
            "titulo": video['informacoes']['items'][0]['snippet']['title'],
            "idioma": None, #video['informacoes']['items'][0]['snippet']['defaultAudioLanguage'] None,
            "descricao": video['informacoes']['items'][0]['snippet']['description'],
            "palavras_chave": None,
            "cobertura": None, #região
            "estrutura": "átomo",
            "nivel_de_agregacao": "2",
            "subnivel_de_agregacao": "e",
            "outros_termos": None,
            "termos": None,
        }
        self.ciclo_de_vida = {
            "versao": None, #video['informacoes']['items'][0]['snippet']['defaultAudioLanguage'],
            "status": "final",
            "contribuinte": {
                "entidade": "Youtube", 
                "papel": "Distribuição", 
                "data": video['informacoes']['items'][0]['snippet']['publishedAt']
            }
        }
        self.meta_metadados = {
            "identificador": {
                "catalogo": "URI",
                "entrada": None #uri deste serviço
            },
            "contribuinte": {
                "entidade": None, #usuario que criou o objeto
                "data": None, #data da criacao
                "papel": None,#papel do usuário
            },
            "esquema_de_metadados": "LOMv1.0",
            "idioma": "Português"
        }
        self.dados_tecnicos = {
            "formato": "video",
            "tamanho": None, #tamanho do vido em bytes
            "localizacao":None, #url deste LOM
            "requisitos": None, #Capacidade técnica necessário para acessar esse objeto
            "ou_composto": {
                "tipo": None,
                "nome": None,
                "versao_minima": None,
                "versao_maxima": None,
            },
            "observacoes_de_instalacao": None,
            "outros_requisitos_de_sistema": None,
            "duracao": None
        }
        self.aspectos_educacionais = {
            "tipo_de_interatividade": "Expositiva",
            "tipo_de_recurso_de_aprendizado": "Vídeo",
            "nivel_de_interatividade": "Baixa",
            "densidade_semantica": None,
            "usuario_final": "Público geral",
            "contexto_de_aprendizagem": None,
            "idade_recomendada": None,
            "grau_de_dificuldade": None,
            "tempo_de_aprendizado": None,
            "intervalo_de_tempo_de_aprendizado": None,
            "descricao": video['comentarios'],
            "linguagem": None,
            "dominio_cognitivo": None,
            "estrategia_cognitiva": None,

        }
        self.direitos = {
            "custo": "Não",
            "direitos_autorais": "Sim",
            "descricao": "Este objeto de aprendizagem é de uso livre"
        }
        self.relacoes = {
            "tipo": None,
            "recurso": None,
            "identificador": {
                "catalogo": "URI",
                "entrada": "http://127.0.0.1:5000/"
            },
            "descricao": None
        }
        self.anotacoes = {
            "entidade": None,
            "data": None,
            "descricao": None
        }
        self.classificacao = {
            "proposito": None,
            "caminho_taxon": {
                "fonte":None,
                "taxon": None,
                "id": None,
                "entrada": None
            },
            "descricao": None,
            "palavras_chave": None,
        }
        self.conteudo = {
            "imagem_padrao": video['informacoes']['items'][0]['snippet']['thumbnails']['default']['url'],
        }
    

    def get_as_json(self):
        return self.__dict__
