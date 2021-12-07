import spacy
from spacy.lang.pt.stop_words import STOP_WORDS
STOP_WORDS.update(['pra', 'pro', 'dele', 'dela'])

class Pln():
    def __init__(self):
        self.pln = spacy.load("pt_core_news_sm")

    def obterDocumentoPln(self, comentarios):
        stringComentarios = " ".join(comentario for comentario in comentarios)
        documentoPnl = self.pln(stringComentarios)
        return documentoPnl

    def identificarStringUnicaLetra(self, string):
        string = list(string.lower())
        primeiraLetra = string[0]
        for letra in string:
            if primeiraLetra != letra:
                return False
        return True

    def obterPalavras(self, comentarios):
        palavras = []
        comentariosPln = self.obterDocumentoPln(comentarios)
        for token in comentariosPln:
            if token.pos_ not in ['PUNCT', 'SIMB', 'X',
                                  'EOL', 'SPACE', 'PART',
                                  'NUM'] and len(token.text) > 2 and not self.identificarStringUnicaLetra(token.text):
                palavras.append(token.text)
        return palavras

    def removerStopWords(self, palavras):
        listaSemStopWords = []
        palavrasPln = self.obterDocumentoPln(palavras)
        for token in palavrasPln:
            if token.text.lower() not in STOP_WORDS:
                listaSemStopWords.append(token.text.lower())
        return listaSemStopWords

    def obterPalavrasChave(self, comentarios, quantidade):
        # testeEnt = self.obterDocumentoPln(comentarios)
        palavras = self.obterPalavras(comentarios)
        palavrasSemStopWords = self.removerStopWords(palavras)
        contadorPalavras = []
        documento = " ".join(palavra for palavra in palavrasSemStopWords)
        for palavra in palavrasSemStopWords:
            palavraIncluida = False
            for objeto in contadorPalavras:
                if objeto['palavra'] == palavra:
                    palavraIncluida = True
                    break
            if not palavraIncluida:
                contadorPalavras.append(
                    {"palavra": palavra, "ocorrencias": documento.count(' ' + palavra + ' ')})
        contadorPalavras.sort(key=lambda objeto: objeto['ocorrencias'])
        palavrasChave = []
        for i in range(quantidade):
            if contadorPalavras:
                if contadorPalavras[-1]['ocorrencias'] > 1: 
                    palavrasChave.append(contadorPalavras.pop()['palavra'])
            else:
                break
        # print(palavrasChave)
        # print("\n================================")
        # print(testeEnt.ents)
        return(palavrasChave)
