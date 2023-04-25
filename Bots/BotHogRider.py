from Bots.Bot import Bot
from abc import ABC, abstractmethod
import random as r

class BotHogRider(Bot):
    def __init__(self, nome, comandos):
        comandos = {"Qual seu nome?" : "O QUÊÊÊ QUANTAS DEFESAS EU JA DESTRUI? WOW, MUITAS! Obrigado por perguntar, agora vai embora",
                    "Qual sua idade?": "Tenho 38 Marretas e 35 porcos HOG RIDAAA, e dai?",
                    "Onde eu moro? ": "A partir do Th7, espero que seja a ultima pergunta por que não estou aguentando mais",
                    "Qual o dia do seu aniversário? " : "30/02 HOG RIDAAAA",
                    "Conte-me uma historia" : "Era uma vez 3 porquinho level 150 e um Th8, o Th8 assustado, pediu socorro, mas nenhum base-builder conseguia salva-lo. Fim da história, agora vai embora. HOG RIDAAAAAA"                   
                    }
        super().__init__(nome, comandos)

    def apresentacao(self):
        print(f"Olá eu sou o {self.__nome} do clash of clans HOG RIDAAAAA, adoro destruir tudo e hoje estou com muita raiva")

    def boas_vindas(self):
        print("Não acredito que me escolheu, em minha terra chamam isso de noobice")

    def despedida(self):
        print("Até que enfim, já não tava aguentando, HOG RIDAAAA")