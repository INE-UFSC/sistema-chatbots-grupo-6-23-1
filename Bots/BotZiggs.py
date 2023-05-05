from Bots.Bot import Bot
from SistemaChatBot.Comando import Comando
class BotZiggs(Bot):
    def __init__(self, nome):
        # do json to get the messages and answers
        comandos = {"Quem eh voce?": "Eu sou Ziggs",
                    "Quantos anos voce existe no LoL?": "Eu circulo pelos campos da justiça durante 11 anos, desde 2012",
                    "Quantas skins voce possui?": "Eu tenho 9 skin dentro de League of Legends, sendo a mais rara a skin Hextec",
                    "Quem voce mais odeia?":"Eu odeio aquele noxiano chamado Draven!!"}
        super().__init__(nome,comandos)


    def apresentacao(self):
        return(f"Meu nome é {super().nome} alguem quer jogar?")

    def boas_vindas(self):
        return(f"{super().nome} diz: Você me escolheu, esta partida será um estouro!")
    
    def despedida(self):
        return(f"{super().nome} diz: não acredito que nosso tempo acabou, estou indo, estou indo !!")