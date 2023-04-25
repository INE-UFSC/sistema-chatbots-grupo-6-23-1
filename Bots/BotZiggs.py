from Bots.Bot import Bot

class BotZiggs(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)

    def apresentacao(self):
        print("Meu nome é" ,self.__nome, "alguem quer jogar?")
            
    def boas_vindas(self):
        print(self.__nome, "diz: Você me escolheu, esta partida será um estouro!")
    
    def despedida(self):
        print(self.__nome,"diz: não acredito que nosso tempo acabou, estou indo, estou indo !!")