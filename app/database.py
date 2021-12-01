from pymongo import MongoClient
from bson.objectid import ObjectId

class Database():
    def __init__(self, nameDb):
        self.client = MongoClient('localhost', 27017)
        self.database = self.client[str(nameDb)]

    @property
    def is_online(self):
        return bool(self.server_status['ok'])

    @property
    def stats(self):
        return self.database.command("dbstats")

    @property
    def server_status(self):
        return self.database.command("serverStatus")

    @property
    def collections(self):
        return self.database.nomeColecaos()

    def list(self, nomeColecao):
        return list(self.database[str(nomeColecao)].find())

    def inserir(self, nomeColecao, objeto):
        self.database[str(nomeColecao)].insert(objeto.get_as_json())

    def buscarObjeto(self, nomeColecao, objetoId):
        return self.database[str(nomeColecao)].find_one({"_id": ObjectId(objetoId)})

    def filtrar(self, nomeColecao, termo):
        return list(self.database[str(nomeColecao)].find(termo))

    def update(self, nomeColecao, objeto):
        objeto = dict(objeto)
        self.database[str(nomeColecao)].update_one({"_id": objeto["_id"]}, {"$set": objeto})

    def delete(self, nomeColecao, objeto):
        self.database[str(nomeColecao)].delete_one({"_id": objeto["_id"]})

