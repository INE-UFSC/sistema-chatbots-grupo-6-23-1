from py_env import run_env

run_env()

#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotHogRider import BotHogRider
from Bots.BotZiggs import BotZiggs
from Bots.BotChatGpt import BotChatGpt

###construa a lista de bots disponíveis aqui
lista_bots = [BotZiggs("Ziggs"), BotHogRider("Hog Ridder"), BotChatGpt("Harry Potter")]
    
sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
