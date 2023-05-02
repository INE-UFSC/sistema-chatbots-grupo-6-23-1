import os
import openai
from Bots.Bot import Bot

class BotChatGpt(Bot):
    def __init__(self, nome):
        comandos = {"Pergunte qualquer coisa": ""}
        super().__init__(nome, comandos)

    def apresentacao(self):
        return self.__gpt_call(f"Apresente-se brevemente, sem dar spoilers, como se você fosse {self.nome} em até no máximo 25 palavras")

    def boas_vindas(self):
        return  self.__gpt_call(f"Dê boas vindas como se você fosse {self.nome}")
    
    def despedida(self):
        return self.__gpt_call(f"Escreva uma mensagem de despedida como se você fosse {self.nome}")
    
    def executa_comando(self, cmd):
        keys = list(self.comandos.keys())

        if keys[cmd-1] == "Pergunte qualquer coisa":
            pergunta = input("Faça uma pergunta: ")
            gpt_query = f"Responda a seguinte pergunta como se você fosse {self.nome}: {pergunta}"

            print(self.__gpt_call(gpt_query))

    def __gpt_call(self, cmd):
        try:
            openai.api_key = os.getenv("API_KEY")
            openai.Model.list()

            res = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": cmd}
                ]
            )

            return res.choices[0]["message"]["content"]
        except:
            print("Error: Chave utilizada, invalida")