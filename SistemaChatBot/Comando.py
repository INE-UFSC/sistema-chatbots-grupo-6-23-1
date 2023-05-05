class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, msg, resposta):
        self.__msg = msg
        self.__resposta = resposta
   
    # get mensagem
    def mensagem(self):
        return  self.__msg

    def responde(self):
        return self.__resposta