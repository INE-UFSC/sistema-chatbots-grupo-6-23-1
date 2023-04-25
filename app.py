#encoding: utf-8
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotHogRider import BotHogRider
from Bots.BotZiggs import BotZiggs

###construa a lista de bots disponíveis aqui
lista_bots = [BotZiggs("Ziggs"), BotHogRider("Hod Ridder")]

sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
