from Bots.Bot import Bot

class BotZiggs(Bot):
    def __init__(self, nome):
        comandos = {"Quem eh voce?": "Eu sou Ziggs",
                    "Quantos anos voce existe no LoL?": "Eu circulo pelos campos da justiça durante 11 anos, desde 2012",
                    "Quantas skins voce possui?": "Eu tenho 9 skin dentro de League of Legends, sendo a mais rara a skin Hextec",
                    "Quem voce mais odeia?":"Eu odeio aquele noxiano chamado Draven!!"}
        super().__init__(nome,comandos)


    def apresentacao(self):
        print("Meu nome é" ,self.__nome, "alguem quer jogar?")
            
    def boas_vindas(self):
        print(self.__nome, "diz: Você me escolheu, esta partida será um estouro!")
    
    def despedida(self):
        print(self.__nome,"diz: não acredito que nosso tempo acabou, estou indo, estou indo !!")