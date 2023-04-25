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

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def mostra_comandos(self):
        keys = list(self.__comandos.keys())

        for index, key in enumerate(keys):
            print(f"{index + 1} - {key}")

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass