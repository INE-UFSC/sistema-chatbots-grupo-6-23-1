from Bots.Bot import Bot
from abc import ABC, abstractmethod
import random as r

class BotHogRider(Bot):
    def __init__(self, nome, comandos):
        super().__init__(nome, comandos)

    def apresentacao(self):
        print(f"Olá eu sou o {self.__nome} do clash of clans HOG RIDAAAAA, adoro destruir tudo e hoje estou com muita raiva")

    def boas_vindas(self):
        print("Não acredito que me escolheu, em minha terra chamam isso de noobice")

    def despedida(self):
        print("Até que enfim, já não tava aguentando, HOG RIDAAAA")