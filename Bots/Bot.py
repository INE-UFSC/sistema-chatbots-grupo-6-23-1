##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):
    def __init__(self, nome, comandos = {}):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome
    
    @property
    def comandos(self):
        return self.__comandos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        keys = list(self.__comandos.keys())

        for index, key in enumerate(keys):
            print(f"{index + 1} - {key}")

    def executa_comando(self, cmd):
        keys = list(self.__comandos.keys())
        print(self.__comandos[keys[cmd-1]])

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass