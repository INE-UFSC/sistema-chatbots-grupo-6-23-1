class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas = []):
        self.__id = id
        self.__msg = msg

    # get id
    def id(self):
        return self.__id
    # get mensagem
    def mensagem(self):
        return  self.__msg

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        pass

    # adiciona resposta
    def addResposta(self, resposta):
        pass
    # remove resposta (opcional)
    def delResposta(self, resposta):
        pass